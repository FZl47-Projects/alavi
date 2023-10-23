from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from package.mixins import PackageRequiredMixin
from .models import DietProgram


class UserDietProgram(LoginRequiredMixin, PackageRequiredMixin, TemplateView):
    template_name = 'program/diet-program.html'
    package_type = 'diet'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)

        pk = kwargs.get('pk')
        program = get_object_or_404(DietProgram, pk=pk)

        contexts['diet_program'] = program
        return contexts


# class DietUserAdd(View):
#
#     @admin_required_cbv()
#     def post(self, request, user_id):
#         user = get_object_or_404(User, id=user_id)
#         data = request.POST.copy()
#
#         food_ids = data.getlist('food', [])
#         days = data.getlist('day', [])
#         foods = Food.objects.filter(id__in=food_ids)
#
#         for day in days:
#             for food in foods:
#                 data_detail = data
#                 data_detail['user'] = user
#                 data_detail['day'] = day
#                 data_detail['food'] = food
#                 f = DietProgramAdd(data_detail)
#                 if form_validate_err(request, f) is False:
#                     return redirect(user.get_absolute_url())
#                 f.save()
#
#         # Create notify for user
#         NotificationUser.objects.create(
#             type='DIET_PROGRAM_ADD',
#             to_user=user,
#             title='برنامه غذایی جدید برای شما ثبت شده است',
#             description="""
#                             برنامه غذایی جدید برای شما ثبت شده است
#                         """,
#             send_notify=True
#         )
#
#         messages.success(request, 'برنامه غذایی با موفقیت ثبت شد')
#         return redirect(user.get_absolute_url())
