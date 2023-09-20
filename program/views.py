from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from requests import request
from account.models import User
from program.models import Days
from program.models import Training_program_object
from program.models import Diet_program_object


# Create your views here.

class Exercies(LoginRequiredMixin,View):
    template_name = 'program/exercise.html'
    def get(self,request):
        user = request.user
        program = user.days.training_program_objects
        context = {
            'user' : user,
            'program' : program
        }
        return render(request,self.template_name, context)

class Diet_plan(View):
    template_name = 'program/diet-plan.html'
    def get(self,request):
        return render(request,self.template_name)