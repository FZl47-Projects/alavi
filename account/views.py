
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .models import User


class Login(View):

    def get(self,request):
        return render(request,'account/login.html')

    def post(self,request):
        post = request.POST
        phonenumber = post["phonenumber"]
        password = post["password"]

        user = authenticate(request, phonenumber=phonenumber, password=password)
        if user is not None:
            login(request, user)
            #return redirect()


class Signup(View):
    def get(self,request):
        return render(request,'account/signup.html')
    
    def post(self, request):
        post = request.POST
        firstname = post["firstname"]
        lastname = post["lastname"]
        phonenumber = post["phonenumber"]
        password = post["password"]
        password2 = post["password2"]

        if User.objects.filter(phonenumber=phonenumber).exists():
            #eror
            pass
        if password == password2:
            new_user = User(first_name=firstname,last_name=lastname,phonenumber=phonenumber)
            new_user.set_password(password)
            new_user.save()
            return redirect('account:login')


class ResetPassword(View):

    def get(self,request):
        return render(request,'account/resetpassword.html')
    
    def post(self, request):
        pass
