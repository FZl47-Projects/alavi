from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from requests import request
from account.models import User
from program.models import Day
from program.models import Training_program_object
from program.models import Diet_program_object


# Create your views here.

class Exercies(LoginRequiredMixin,View):
    template_name = 'program/exercise.html'
    def get(self,request):
        user = request.user
        programs0 =  user.user_training_program.filter(day='0')
        programs1 =  user.user_training_program.filter(day='0')
        programs2 =  user.user_training_program.filter(day='2')
        programs3 =  user.user_training_program.filter(day='3')
        programs4 =  user.user_training_program.filter(day='4')
        programs5 =  user.user_training_program.filter(day='5')
        programs6 =  user.user_training_program.filter(day='6')
        context  = {
            'user' : user,
            'programs0' : programs0,
            'programs1' : programs1,
            'programs2' : programs2,
            'programs3' : programs3,
            'programs4' : programs4,
            'programs5' : programs5,
            'programs6' : programs6,
        }
        return render(request,self.template_name, context)

class Diet_plan(View):
    template_name = 'program/diet-plan.html'
    def get(self,request):
        user = request.user
        programs0 =  user.user_diet_program.filter(day='0')
        programs1 =  user.user_diet_program.filter(day='1')
        programs2 =  user.user_diet_program.filter(day='2')
        programs3 =  user.user_diet_program.filter(day='3')
        programs4 =  user.user_diet_program.filter(day='4')
        programs5 =  user.user_diet_program.filter(day='5')
        programs6 =  user.user_diet_program.filter(day='6')
        context  = {
            'user' : user,
            'programs0' : programs0,
            'programs1' : programs1,
            'programs2' : programs2,
            'programs3' : programs3,
            'programs4' : programs4,
            'programs5' : programs5,
            'programs6' : programs6,
        }
        return render(request,self.template_name, context)
