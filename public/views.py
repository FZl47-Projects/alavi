from django.shortcuts import render
from django.views.generic import View
from requests import request
from account.models import User

class Index(View):
    template_name = 'public/index.html'

    def get(self,request):
        return render(request,self.template_name)

