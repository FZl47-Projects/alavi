from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest, Http404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth import authenticate, login, get_user_model, logout as logout_handler
from core.utils import add_prefix_phonenum, random_num, form_validate_err
from core.auth.decorators import admin_required_cbv
from core.redis_py import set_value_expire, remove_key, get_value
from notification.models import NotificationUser
from program.models import Food, Sport, DietProgramFree
from public.models import Certificate
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
            messages.success(request, 'خوش امدید')
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
        # login
        login(request, user)
        messages.success(request, 'حساب شما با موفقیت ایجاد شد')
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
        context = {
            'users': users
        }
        return render(request, self.template_name, context)


class Sports(View):
    template_name = 'account/admin/sports.html'

    @admin_required_cbv()
    def get(self, request):
        sports = Sport.objects.all()
        context = {
            'sports': sports
        }
        return render(request, self.template_name, context)


class Certificates(View):
    template_name = 'account/admin/certificates.html'

    @admin_required_cbv()
    def get(self, request):
        certificates = Certificate.objects.all()
        context = {
            'certificates': certificates
        }
        return render(request, self.template_name, context)


class CertificateAdd(View):

    @admin_required_cbv()
    def post(self, request):
        data = request.POST
        f = forms.CertificateAdd(data, request.FILES)
        if form_validate_err(request, f) is False:
            return redirect('account:certificates')
        f.save()
        messages.success(request, 'مدرک با موفقیت اضافه شد')
        return redirect('account:certificates')


class CertificateDelete(View):

    @admin_required_cbv()
    def get(self, request, certificate_id):
        certificate = get_object_or_404(Certificate, id=certificate_id)
        certificate.delete()
        messages.success(request, 'مدرک با موفقیت حذف شد')
        return redirect('account:certificates')


class DefinitionDietFree(LoginRequiredMixin, View):
    template_name = 'account/admin/definition-of-diet-free.html'

    @admin_required_cbv()
    def get(self, request):
        programs0 = DietProgramFree.objects.filter(day='0')
        programs1 = DietProgramFree.objects.filter(day='1')
        programs2 = DietProgramFree.objects.filter(day='2')
        programs3 = DietProgramFree.objects.filter(day='3')
        programs4 = DietProgramFree.objects.filter(day='4')
        programs5 = DietProgramFree.objects.filter(day='5')
        programs6 = DietProgramFree.objects.filter(day='6')

        context = {
            'programs0': programs0,
            'programs1': programs1,
            'programs2': programs2,
            'programs3': programs3,
            'programs4': programs4,
            'programs5': programs5,
            'programs6': programs6,
            'foods': Food.objects.all()
        }
        return render(request, self.template_name, context)

    @admin_required_cbv()
    def post(self, request):
        data = request.POST.copy()
        food_ids = data.getlist('food', [])
        days = data.getlist('day', [])
        foods = Food.objects.filter(id__in=food_ids)
        for day in days:
            for food in foods:
                data_detail = data
                data_detail['day'] = day
                data_detail['food'] = food
                f = forms.DietProgramFreeAdd(data_detail)
                if form_validate_err(request, f) is False:
                    return redirect('account:definition-of-diet-free')
                f.save()
        messages.success(request, 'برنامه غذایی رایگان با موفقیت ثبت شد')
        return redirect('account:definition-of-diet-free')


class DefinitionDietFreeDelete(LoginRequiredMixin, View):

    @admin_required_cbv()
    def get(self, request, diet_free_id):
        diet_obj = get_object_or_404(DietProgramFree, id=diet_free_id)
        diet_obj.delete()
        messages.success(request, 'برنامه غذایی با موفقیت حذف شد')
        return redirect('account:definition-of-diet-free')


class DefinitionDiet(LoginRequiredMixin, View):
    template_name = 'account/admin/definition-of-diet.html'

    @admin_required_cbv()
    def get(self, request):
        context = {
            'users': User.normal_user.all(),
            'foods': Food.objects.all()
        }
        return render(request, self.template_name, context)

    @admin_required_cbv()
    def post(self, request):
        data = request.POST.copy()
        user_ids = data.getlist('user', [])
        food_ids = data.getlist('food', [])
        days = data.getlist('day', [])
        foods = Food.objects.filter(id__in=food_ids)
        users = User.normal_user.filter(id__in=user_ids)
        for user in users:
            for day in days:
                for food in foods:
                    data_detail = data
                    data_detail['user'] = user
                    data_detail['day'] = day
                    data_detail['food'] = food
                    f = forms.DietProgramAdd(data_detail)
                    if form_validate_err(request, f) is False:
                        return redirect('account:definition-of-diet')
                    f.save()
            # create notify for user
            NotificationUser.objects.create(
                type='DIET_PROGRAM_ADD',
                to_user=user,
                title='برنامه غذایی جدید برای شما ثبت شده است',
                description="""
                        برنامه غذایی جدید برای شما ثبت شده است
                    """,
                send_notify=True
            )

        messages.success(request, 'برنامه غذایی با موفقیت ثبت شد')
        return redirect('account:definition-of-diet')


class DefinitionTrainingProgram(LoginRequiredMixin, View):
    template_name = 'account/admin/definition-of-training-program.html'

    @admin_required_cbv()
    def get(self, request):
        context = {
            'users': User.normal_user.all(),
            'sports': Sport.objects.all()
        }
        return render(request, self.template_name, context)

    @admin_required_cbv()
    def post(self, request):
        data = request.POST.copy()
        user_ids = data.getlist('user', [])
        sport_ids = data.getlist('sport', [])
        days = data.getlist('day', [])
        sports = Sport.objects.filter(id__in=sport_ids)
        users = User.normal_user.filter(id__in=user_ids)
        for user in users:
            for day in days:
                for sport in sports:
                    data_detail = data
                    data_detail['user'] = user
                    data_detail['day'] = day
                    data_detail['sport'] = sport
                    f = forms.TrainingProgramAdd(data_detail)
                    if form_validate_err(request, f) is False:
                        return redirect('account:definition-of-training-program')
                    f.save()
            # create notify for user
            NotificationUser.objects.create(
                type='TRAINING_PROGRAM_ADD',
                to_user=user,
                title='برنامه تمرینی جدید برای شما ثبت شده است',
                description="""
                            برنامه تمرینی جدید برای شما ثبت شده است
                        """,
                send_notify=True
            )
        messages.success(request, 'برنامه تمرینی با موفقیت ثبت شد')
        return redirect('account:definition-of-training-program')


class UserProfile(LoginRequiredMixin, View):
    template_name = 'account/user-profile.html'

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user.is_normal_user and user != request.user:
            raise Http404
        context = {
            'user_detail': user,
            'sports': Sport.objects.all(),
            'foods': Food.objects.all()
        }
        return render(request, self.template_name, context)


class UserProfileUpdate(LoginRequiredMixin, View):

    def post(self, request):
        data = request.POST.copy()
        # set data
        user = request.user
        data['user'] = user
        user_info = None
        try:
            user_info = user.info
        except:
            pass
        f = forms.UserUpdateInfoForm(data, request.FILES, instance=user_info)
        if form_validate_err(request, f) is False:
            return redirect(user.get_absolute_url())
        f.save()
        messages.success(request, 'مشخصات شما با موفقیت بروزرسانی شد')
        return redirect(user.get_absolute_url())


class UserProfileDelete(LoginRequiredMixin, View):

    @admin_required_cbv()
    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.delete()
        messages.success(request, 'کاربر موفقیت حذف شد')
        return redirect('account:users')
