from django.contrib.auth import authenticate, login, get_user_model, logout as logout_handler
from django.http import JsonResponse, HttpResponseBadRequest, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.utils.translation import gettext as _
from django.views.generic import View
from django.contrib import messages
from django.conf import settings

from apps.core.utils import add_prefix_phonenum, random_num, form_validate_err
from apps.core.redis_py import set_value_expire, remove_key, get_value
from apps.core.auth.decorators import admin_required_cbv
from apps.notification.models import NotificationUser
from .models import ExerciseDay, UserProfile
from .mixins import LogoutRequiredMixin
from . import forms
import json

User = get_user_model()
RESET_PASSWORD_CONFIG = settings.RESET_PASSWORD_CONFIG


def login_register(request):
    def login_perform(request, data):
        user = None
        phonenumber = data.get('phonenumber', None)
        password = data.get('password', None)
        if phonenumber and password:
            phonenumber = add_prefix_phonenum(phonenumber)
            user = authenticate(request, username=phonenumber, password=password)
            if user is None:
                messages.error(request, 'کاربری با این مشخصات یافت نشد')
                return redirect('account:login_register')

            login(request, user)
            messages.success(request, _('Welcome'))

            return redirect('public:index')
        else:
            messages.error(request, 'لطفا فیلد هارا به درستی وارد نمایید')

        return redirect(user.get_absolute_url())

    def register_perform(request, data):
        f = forms.RegisterUserForm(data=data)
        if f.is_valid() is False:
            messages.error(request, 'لطفا فیلد هارا به درستی وارد نمایید')
            return redirect('account:login_register')

        # check for exists normal_user
        phonenumber = f.cleaned_data['phonenumber']
        if User.objects.filter(phonenumber=phonenumber).exists():
            messages.error(request, 'کاربری با این شماره از قبل ثبت شده است')
            return redirect('account:login_register')

        # create user
        password = f.cleaned_data['password2']
        user = User(
            phonenumber=phonenumber,
            first_name=f.cleaned_data['first_name'],
            last_name=f.cleaned_data['last_name'],
        )
        user.set_password(password)
        user.save()

        # Login user and redirect to index page
        login(request, user)

        messages.success(request, _('Welcome'))

        return redirect('public:index')

    if request.method == 'GET':
        return render(request, 'account/login-register.html')

    elif request.method == 'POST':
        data = request.POST
        type_page = data.get('type-page', 'login')

        if type_page == 'login':
            return login_perform(request, data)
        elif type_page == 'register':
            return register_perform(request, data)


# Render UserProfileInfo View
class GetUserProfileInfo(View):
    """ Get UserProfile info before finishing user register """
    def get(self, request):
        # Get register_token and get profile
        try:
            token = request.session.get('register_token')

            profile = UserProfile.objects.get(token=token)
            if profile.verified:
                return redirect('public:index')
        except UserProfile.DoesNotExist:
            raise Http404

        return render(request, 'account/profile-info-form.html', {'profile': profile})

    def post(self, request):
        data = request.POST
        try:
            profile = UserProfile.objects.get(token=data.get('token'))
        except (UserProfile.DoesNotExist, KeyError):
            raise Http404

        # Get exercise days and set them in profile
        selected_days = data.getlist('exercise_days')
        days = ExerciseDay.objects.filter(name__in=selected_days)
        profile.exercise_days.set(days)

        form = forms.UserProfileInfoForm(data, request.FILES, instance=profile)
        if not form_validate_err(request, form):
            return redirect(reverse('account:register_profile'))
        form.save()

        # Remove register_token
        profile.clear_token(request)

        messages.success(request, _('Information registered successfully'))

        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)

        return redirect('public:index')


def logout(request):
    logout_handler(request)
    return redirect('public:index')


def reset_password(request):
    return render(request, 'account/reset-password.html')


@require_POST
def reset_password_send(request):
    # AJAX view
    data = json.loads(request.body)
    phonenumber = data.get('phonenumber', None)
    # validate data
    if not phonenumber:
        return HttpResponseBadRequest()
    # check user is exists
    try:
        phonenumber = add_prefix_phonenum(phonenumber)
        user = User.objects.get(phonenumber=phonenumber)
    except:
        raise Http404
    code = random_num(RESET_PASSWORD_CONFIG['CODE_LENGTH'])
    key = RESET_PASSWORD_CONFIG['STORE_BY'].format(phonenumber)
    # check code state set
    if get_value(key) is not None:
        # code is already set
        return HttpResponse(status=409)
    # set code
    set_value_expire(key, code, RESET_PASSWORD_CONFIG['TIMEOUT'])
    # send code
    NotificationUser.objects.create(
        type='RESET_PASSWORD_CODE_SENT',
        kwargs={
            'code': code
        },
        to_user=user,
        title='بازیابی رمز عبور',
        description=f"""
             کد بازیابی رمز عبور : 
             {code}
        """,
        send_notify=True
    )
    return JsonResponse({})


@require_POST
def reset_password_check(request):
    # AJAX view
    data = json.loads(request.body)
    phonenumber = data.get('phonenumber', None)
    code = data.get('code', None)
    # validate data
    if (not code) or (not phonenumber):
        return HttpResponseBadRequest()
    phonenumber = add_prefix_phonenum(phonenumber)
    key = RESET_PASSWORD_CONFIG['STORE_BY'].format(phonenumber)
    # check code
    code_stored = get_value(key)
    if code_stored is None:
        # code is not seted or timeout
        return HttpResponse(status=410)
    if code_stored != code:
        # code is wrong(not same)
        return HttpResponse(status=409)
    return JsonResponse({})


@require_POST
def reset_password_set(request):
    # AJAX view
    data = json.loads(request.body)
    f = forms.ResetPasswordSetForm(data)

    # Validate data
    if f.is_valid() is False:
        return HttpResponseBadRequest()
    clean_data = f.cleaned_data

    # phonenumber must get from data (not clean_data)
    phonenumber = data['phonenumber']
    code = clean_data['code']
    password = clean_data['password2']
    # check user is exists
    try:
        phonenumber = add_prefix_phonenum(phonenumber)
        user = User.objects.get(phonenumber=phonenumber)
    except:
        raise Http404
    key = RESET_PASSWORD_CONFIG['STORE_BY'].format(phonenumber)
    # check code
    code_stored = get_value(key)
    if code_stored is None:
        # code is not seted or timeout
        return HttpResponse(status=410)
    if code_stored != code:
        # code is wrong(not same)
        return HttpResponse(status=409)
    user.set_password(password)
    user.save()
    remove_key(key)
    NotificationUser.objects.create(
        type='PASSWORD_CHANGED_SUCCESSFULLY',
        to_user=user,
        title='رمز عبور شما تغییر کرد',
        description="""
            رمز عبور شما با موفقیت تغییر کرد
        """,
        send_notify=True
    )
    return JsonResponse({})


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'account/user-profile.html'

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user.is_normal_user and user != request.user:
            raise Http404

        return render(request, self.template_name, context={'user_detail': user,})


class UserProfileUpdate(LoginRequiredMixin, View):
    def post(self, request):
        data = request.POST.copy()

        # set data
        user = request.user
        data['user'] = user
        profile = None
        try:
            profile = user.user_profile
        except (AttributeError, ValueError):
            pass

        form = forms.UserProfileUpdateForm(data, request.FILES, instance=profile)
        if form_validate_err(request, form) is False:
            return redirect(user.get_absolute_url())
        form.save()

        messages.success(request, 'مشخصات شما با موفقیت بروزرسانی شد')
        return redirect(user.get_absolute_url())


class UserProfileDelete(LoginRequiredMixin, View):

    @admin_required_cbv()
    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.delete()

        messages.success(request, 'کاربر موفقیت حذف شد')
        return redirect('account:users')


class HomeAdmin(View):
    template_name = 'account/admin/home-admin.html'

    @admin_required_cbv()
    def get(self, request):
        return render(request, self.template_name)


class Users(View):
    template_name = 'account/admin/users.html'

    @admin_required_cbv()
    def get(self, request):
        users = User.normal_user.all()

        return render(request, self.template_name, context={'users': users})
