from django.shortcuts import render
from django.views.generic import View
from . import models


class Index(View):
    template_name = 'public/index.html'

    def get(self, request):
        context = {
            'certificates': models.Certificate.objects.all()
        }
        return render(request, self.template_name, context)


# class DietFree(View):
#     template_name = 'public/diet-free.html'
#
#     def get(self, request):
#         programs0 = DietProgramFree.objects.filter(day='0')
#         programs1 = DietProgramFree.objects.filter(day='1')
#         programs2 = DietProgramFree.objects.filter(day='2')
#         programs3 = DietProgramFree.objects.filter(day='3')
#         programs4 = DietProgramFree.objects.filter(day='4')
#         programs5 = DietProgramFree.objects.filter(day='5')
#         programs6 = DietProgramFree.objects.filter(day='6')
#
#         context = {
#             'programs0': programs0,
#             'programs1': programs1,
#             'programs2': programs2,
#             'programs3': programs3,
#             'programs4': programs4,
#             'programs5': programs5,
#             'programs6': programs6,
#             'foods': Food.objects.all()
#         }
#         return render(request, self.template_name, context)
