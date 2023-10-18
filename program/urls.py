from django.urls import path
from . import views


app_name = 'program'

urlpatterns = [
    path('exercise/<user_id>', views.Exercises.as_view(), name='exercise'),
    path('diet-plan/<user_id>', views.DietPlan.as_view(), name='diet-plan'),

    path('exercise', views.Exercises.as_view(), name='exercise'),
    path('diet-plan', views.DietPlan.as_view(), name='diet-plan'),

    path('diet-category/', views.DietProgramCategoryView.as_view(), name='diet_category'),
    path('diet-category/add/', views.AddDietProgramCategoryView.as_view(), name='diet_category_add'),
    path('diet-category/<int:pk>/del/', views.DelDietProgramCategoryView.as_view(), name='diet_category_del'),

    path('food/add', views.FoodAdd.as_view(), name='food_add'),
    path('food/<int:food_id>/delete', views.FoodDelete.as_view(), name='food_delete'),

    path('sport/add', views.SportAdd.as_view(), name='sport_add'),
    path('sport/<int:sport_id>/delete', views.SportDelete.as_view(), name='sport_delete'),

    path('training/<int:user_id>/add', views.TrainingUserAdd.as_view(), name='training-user-add'),
    path('diet/<int:user_id>/add', views.DietUserAdd.as_view(), name='diet-user-add'),
]
