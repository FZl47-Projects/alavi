from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    # login logout and register
    path('login-register',views.login_register,name='login_register'),
    path('logout',views.logout,name='logout'),
    # reset password
    path('reset-password',views.reset_password,name='reset_password'),
    path('reset-password/send-code',views.reset_password_send,name='reset_password_send_code'),
    path('reset-password/check-code',views.reset_password_check,name='reset_password_check_code'),
    path('reset-password/set',views.reset_password_set,name='reset_password_set'),

    # dashboard
    path('dashboard',views.dashboard,name='dashboard'),

    #club admin
    path('club-admin/home-admin', views.Home_admin.as_view(),name='home-admin'),
    path('club-admin/users', views.Users.as_view(),name='users'),
    path('club-admin/definition-of-diet', views.Definition_diet.as_view(),name='definition-of-diet'),
    path('club-admin/definition-of-training-program', views.Definition_training_program.as_view(),name='definition-of-training-program'),
    path('club-admin/user-profile/<int:user_id>', views.User_profile.as_view(),name='user-profile'),

]