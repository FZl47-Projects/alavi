from django.urls import path,include
from . import views

app_name = 'public'

urlpatterns = [
    path('', views.Index.as_view(),name='public'),
    path('exercise', views.Exercies.as_view(),name='exercise'),
    path('diet-plan', views.Diet_plan.as_view(),name='diet-plan'),
    path('club-admin/home-admin', views.Home_admin.as_view(),name='home-admin'),
    path('club-admin/users', views.Users.as_view(),name='users'),
    path('club-admin/definition-of-diet', views.Definition_diet.as_view(),name='definition-of-diet.'),
    path('club-admin/definition-of-training-program', views.Definition_training_program.as_view(),name='definition-of-training-program'),
     path('club-admin/user-profile', views.User_profile.as_view(),name='user-profile'),

]