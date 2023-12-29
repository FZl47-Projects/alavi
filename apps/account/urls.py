from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    # login logout and register
    path('login-register/', views.login_register, name='login_register'),
    path('logout/', views.logout, name='logout'),
    path('register/complete-profile/', views.GetUserProfileInfo.as_view(), name='register_profile'),

    # reset password
    path('reset-password', views.reset_password, name='reset_password'),
    path('reset-password/send-code', views.reset_password_send, name='reset_password_send_code'),
    path('reset-password/check-code', views.reset_password_check, name='reset_password_check_code'),
    path('reset-password/set', views.reset_password_set, name='reset_password_set'),

    # club admin
    path('club-admin/home-admin', views.HomeAdmin.as_view(), name='home-admin'),
    path('club-admin/users', views.Users.as_view(), name='users'),

    path('user-profile/<int:user_id>', views.UserProfileView.as_view(), name='user-profile'),
    path('user-profile/update/', views.UserProfileUpdate.as_view(), name='user_profile_update'),
    path('user-profile/<int:user_id>/delete', views.UserProfileDelete.as_view(), name='user-profile-delete'),
]
