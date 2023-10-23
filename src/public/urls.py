from django.urls import path
from . import views

app_name = 'public'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('diet-free', views.DietFree.as_view(), name='diet_free'),
]
