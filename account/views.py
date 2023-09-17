from django.shortcuts import render
import requests
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)

        inputs_val = [username, password]

        if User.objects.filter(username=username, password=password).exists():
            user = User.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            
    