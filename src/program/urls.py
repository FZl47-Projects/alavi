from django.urls import path
from . import views


app_name = 'program'

urlpatterns = [
    path('exercise-program/<int:pk>/', views.Exercises.as_view(), name='exercise_program'),
    path('diet-program/<int:pk>/', views.UserDietProgram.as_view(), name='diet_program'),

    path('foods/', views.FoodsView.as_view(), name='foods'),
    path('food/add', views.FoodAddView.as_view(), name='food_add'),
    path('food/<int:food_id>/delete/', views.FoodDelete.as_view(), name='food_del'),

    path('sport/add/', views.SportAdd.as_view(), name='sport_add'),
    path('sport/<int:sport_id>/delete/', views.SportDelete.as_view(), name='sport_delete'),

    path('training/<int:user_id>/add/', views.TrainingUserAdd.as_view(), name='training-user-add'),
    path('diet/<int:user_id>/add/', views.DietUserAdd.as_view(), name='diet-user-add'),
]
