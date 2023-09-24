from django.urls import path
from . import views

app_name = 'program'
urlpatterns = [
    path('exercise/<user_id>', views.Exercies.as_view(),name='exercise'),
    path('diet-plan/<user_id>', views.Diet_plan.as_view(),name='diet-plan'),

    path('exercise', views.Exercies.as_view(), name='exercise'),
    path('diet-plan', views.Diet_plan.as_view(), name='diet-plan'),

    path('food/add', views.FoodAdd.as_view(), name='food_add'),
    path('food/<int:food_id>/delete', views.FoodDelete.as_view(), name='food_delete'),

    path('sport/add', views.SportAdd.as_view(), name='sport_add'),
    path('sport/<int:sport_id>/delete', views.SportDelete.as_view(), name='sport_delete'),

    path('training/<int:user_id>/add', views.TrainingUserAdd.as_view(), name='training-user-add'),
    path('diet/<int:user_id>/add', views.DietUserAdd.as_view(), name='diet-user-add'),

]