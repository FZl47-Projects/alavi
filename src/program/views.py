from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.contrib import messages

from core.utils import form_validate_err, add_prefix_phonenum
from core.auth.decorators import admin_required_cbv

from account.forms import TrainingProgramAdd, DietProgramAdd
from account.models import User

from notification.models import NotificationUser
from .models import Food, Sport, DietProgram
from . import forms


class Exercises(LoginRequiredMixin, View):
    template_name = 'program/exercise.html'

    def get(self, request, user_id=None):
        if user_id:
            user = get_object_or_404(User, id=user_id)
            if not request.user.is_admin_user:
                raise Http404
        else:
            user = request.user
            if user.is_admin_user:
                return redirect('account:definition-of-training-program')


        programs0 = user.user_training_program.filter(day='0')
        programs1 = user.user_training_program.filter(day='1')
        programs2 = user.user_training_program.filter(day='2')
        programs3 = user.user_training_program.filter(day='3')
        programs4 = user.user_training_program.filter(day='4')
        programs5 = user.user_training_program.filter(day='5')
        programs6 = user.user_training_program.filter(day='6')
        context = {
            'user_detail': user,
            'programs0': programs0,
            'programs1': programs1,
            'programs2': programs2,
            'programs3': programs3,
            'programs4': programs4,
            'programs5': programs5,
            'programs6': programs6,
        }
        return render(request, self.template_name, context)


class UserDietProgram(LoginRequiredMixin, TemplateView):
    template_name = 'program/diet-program.html'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)

        pk = kwargs.get('pk')
        program = get_object_or_404(DietProgram, pk=pk)

        contexts['diet_program'] = program
        return contexts


class FoodsView(View):
    template_name = 'program/foods.html'

    @admin_required_cbv()
    def get(self, request):
        foods = Food.objects.all()

        # Create template contexts
        context = {'foods': foods}

        return render(request, self.template_name, context)


class FoodAddView(View):

    @admin_required_cbv()
    def post(self, request):
        data = request.POST
        form = forms.FoodAdd(data)

        if form_validate_err(request, form) is False:
            return redirect('program:foods')

        # Add new food
        form.save()
        messages.success(request, 'غذا با موفقیت اضافه شد')

        return redirect('program:foods')


class FoodDelete(View):

    @admin_required_cbv()
    def get(self, request, food_id):
        food = get_object_or_404(Food, id=food_id)
        food.delete()

        messages.success(request, 'غذا با موفقیت حذف شد')

        return redirect('program:foods')


class SportAdd(View):

    @admin_required_cbv()
    def post(self, request):
        data = request.POST

        f = forms.SportAdd(data)
        if form_validate_err(request, f) is False:
            return redirect('account:sports')

        f.save()
        messages.success(request, 'ورزش با موفقیت اضافه شد')
        return redirect('account:sports')


class SportDelete(View):

    @admin_required_cbv()
    def get(self, request, sport_id):
        sport = get_object_or_404(Sport, id=sport_id)
        sport.delete()
        messages.success(request, 'ورزش با موفقیت حذف شد')
        return redirect('account:sports')


class DietUserAdd(View):

    @admin_required_cbv()
    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        data = request.POST.copy()

        food_ids = data.getlist('food', [])
        days = data.getlist('day', [])
        foods = Food.objects.filter(id__in=food_ids)

        for day in days:
            for food in foods:
                data_detail = data
                data_detail['user'] = user
                data_detail['day'] = day
                data_detail['food'] = food
                f = DietProgramAdd(data_detail)
                if form_validate_err(request, f) is False:
                    return redirect(user.get_absolute_url())
                f.save()

        # Create notify for user
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
        return redirect(user.get_absolute_url())


class TrainingUserAdd(View):

    @admin_required_cbv()
    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        data = request.POST.copy()
        sport_ids = data.getlist('sport', [])
        days = data.getlist('day', [])
        sports = Sport.objects.filter(id__in=sport_ids)
        for day in days:
            for sport in sports:
                data_detail = data
                data_detail['user'] = user
                data_detail['day'] = day
                data_detail['sport'] = sport
                f = TrainingProgramAdd(data_detail)
                if form_validate_err(request, f) is False:
                    return redirect(user.get_absolute_url())
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
        return redirect(user.get_absolute_url())
