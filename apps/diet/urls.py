from django.urls import path
from . import views


app_name = 'diet'

urlpatterns = [
    path('diet-program/<int:pk>/', views.UserDietProgram.as_view(), name='diet_program'),
]
