from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('request/', views.PackageRequestView.as_view(), name='package_request'),
]
