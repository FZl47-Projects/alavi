from django.urls import path
from . import views

app_name = 'public'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('free-diet/', views.FreeDietProgramView.as_view(), name='free_diet'),
    path('free-exercise/', views.FreeExerciseProgramView.as_view(), name='free_exercise'),
]
