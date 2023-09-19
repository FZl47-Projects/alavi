from django.shortcuts import render
from django.views.generic import View

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

class Home_admin(View):
    template_name = 'admin/home-admin.html'
    def get(self,request):
        return render(request,self.template_name)

class Users(View):
    template_name = 'admin/users.html'
    def get(self,request):
        return render(request,self.template_name)

class Definition_diet(View):
    template_name = 'admin/definition-of-diet.html'
    def get(self,request):
        return render(request,self.template_name)

class Definition_training_program(View):
    template_name = 'admin/definition-of-training-program.html'
    def get(self,request):
        return render(request,self.template_name)

class User_profile(View):
    template_name = 'admin/user-profile.html'
    def get(self,request):
        return render(request,self.template_name)