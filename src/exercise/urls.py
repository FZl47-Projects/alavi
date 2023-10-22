from django.urls import path
from . import views


app_name = 'exercise'

urlpatterns = [
    path('exercise-program/<int:pk>/', views.UserExerciseProgram.as_view(), name='exercise_program'),
]
