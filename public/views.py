from django.shortcuts import render
from django.views.generic import View
from account.models import User
from program.models import Diet_program_object_free, Food
from . import models


class Index(View):
    template_name = 'public/index.html'

    def get(self, request):
        context = {
            'certificates': models.Certificate.objects.all()
        }
        return render(request, self.template_name, context)


class DietFree(View):
    template_name = 'public/diet-free.html'

    def get(self, request):
        programs0 = Diet_program_object_free.objects.filter(day='0')
        programs1 = Diet_program_object_free.objects.filter(day='1')
        programs2 = Diet_program_object_free.objects.filter(day='2')
        programs3 = Diet_program_object_free.objects.filter(day='3')
        programs4 = Diet_program_object_free.objects.filter(day='4')
        programs5 = Diet_program_object_free.objects.filter(day='5')
        programs6 = Diet_program_object_free.objects.filter(day='6')

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
