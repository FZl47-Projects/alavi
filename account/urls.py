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

    #club admin
    path('club-admin/home-admin', views.Home_admin.as_view(),name='home-admin'),
    path('club-admin/users', views.Users.as_view(),name='users'),
    path('club-admin/foods', views.Foods.as_view(),name='foods'),
    path('club-admin/sports', views.Sports.as_view(),name='sports'),
    path('club-admin/certificates', views.Certificates.as_view(),name='certificates'),
    path('club-admin/certificate/add', views.CertificateAdd.as_view(),name='certificate_add'),
    path('club-admin/certificate/<int:certificate_id>/delete', views.CertificateDelete.as_view(),name='certificate_delete'),
    path('club-admin/definition-of-diet', views.Definition_diet.as_view(),name='definition-of-diet'),
    path('club-admin/definition-of-diet-free', views.Definition_diet_free.as_view(),name='definition-of-diet-free'), # add
    path('club-admin/definition-of-diet-free-delete/<int:diet_free_id>', views.Definition_diet_free_delete.as_view(),name='definition-of-diet-free-delete'),
    path('club-admin/definition-of-training-program', views.Definition_training_program.as_view(),name='definition-of-training-program'),

    path('club-user/user-profile/<int:user_id>', views.User_profile.as_view(),name='user-profile'),
    path('club-user/user-profile/update', views.User_profile_update.as_view(),name='user-profile-update'),
    path('club-user/user-profile/<int:user_id>/delete', views.User_profile_delete.as_view(),name='user-profile-delete'),

]