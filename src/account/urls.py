from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    # login logout and register
    path('login-register', views.login_register, name='login_register'),
    path('logout', views.logout, name='logout'),

    # reset password
    path('reset-password', views.reset_password, name='reset_password'),
    path('reset-password/send-code', views.reset_password_send, name='reset_password_send_code'),
    path('reset-password/check-code', views.reset_password_check, name='reset_password_check_code'),
    path('reset-password/set', views.reset_password_set, name='reset_password_set'),

    # club admin
    path('club-admin/home-admin', views.HomeAdmin.as_view(), name='home-admin'),
    path('club-admin/users', views.Users.as_view(), name='users'),

    path('club-admin/sports', views.Sports.as_view(), name='sports'),

    path('club-admin/certificates', views.Certificates.as_view(), name='certificates'),
    path('club-admin/certificate/add', views.CertificateAdd.as_view(), name='certificate_add'),
    path('club-admin/certificate/<int:certificate_id>/delete', views.CertificateDelete.as_view(), name='certificate_delete'),

    path('club-admin/definition-of-diet', views.DefinitionDiet.as_view(), name='definition-of-diet'),
    path('club-admin/definition-of-diet-free', views.DefinitionDietFree.as_view(), name='definition-of-diet-free'),  # add
    path('club-admin/definition-of-diet-free-delete/<int:diet_free_id>', views.DefinitionDietFreeDelete.as_view(), name='definition-of-diet-free-delete'),

    path('club-admin/definition-of-training-program', views.DefinitionTrainingProgram.as_view(), name='definition-of-training-program'),

    path('user-profile/<int:user_id>', views.UserProfile.as_view(), name='user-profile'),
    path('user-profile/update', views.UserProfileUpdate.as_view(), name='user-profile-update'),
    path('user-profile/<int:user_id>/delete', views.UserProfileDelete.as_view(), name='user-profile-delete'),
]
