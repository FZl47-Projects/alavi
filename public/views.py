from django.shortcuts import render
from django.views.generic import View
from requests import request
from account.models import User

class Index(View):
    template_name = 'public/index.html'

    def get(self,request):
        return render(request,self.template_name)

class Exercies(View):
    template_name = 'public/exercise.html'
    def get(self,request):
        return render(request,self.template_name)

class Diet_plan(View):
    template_name = 'public/diet-plan.html'
    def get(self,request):
        return render(request,self.template_name)