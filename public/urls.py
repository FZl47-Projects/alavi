from django.urls import path,include
from . import views

app_name = 'public'

urlpatterns = [
    path('', views.Index.as_view(),name='public'),

]