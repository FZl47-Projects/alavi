from django.urls import path,include
from . import views

app_name = 'public'

urlpatterns = [
    path('', views.Index.as_view(),name='public'),
    path('exercise', views.Exercies.as_view(),name='exercise'),
    path('diet-plan', views.Diet_plan.as_view(),name='diet-plan'),
    
]