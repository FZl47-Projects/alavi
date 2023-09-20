from django.shortcuts import render
from django.views.generic import View
from requests import request
from account.models import User
from program.models import Days

# Create your views here.

class Exercies(View):
    template_name = 'program/exercise.html'
    def get(self,request):
        user = User.get_user
        context = {
            'user' : user,
        }
        return render(request,self.template_name, context)

class Diet_plan(View):
    template_name = 'program/diet-plan.html'
    def get(self,request):
        return render(request,self.template_name)