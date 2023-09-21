from django.urls import path
from . import views

app_name = 'program'
urlpatterns = [
    path('exercise/<user_id>', views.Exercies.as_view(),name='exercise'),
    path('diet-plan/<user_id>', views.Diet_plan.as_view(),name='diet-plan'),

    path('exercise', views.Exercies.as_view(), name='exercise'),
    path('diet-plan', views.Diet_plan.as_view(), name='diet-plan'),
]