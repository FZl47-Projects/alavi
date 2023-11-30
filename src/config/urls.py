from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.account.views import login_register


urlpatterns = [
    path('admin/login/', login_register, name='login_register'),
    path('admin/', admin.site.urls),
    path('u/', include('apps.account.urls', namespace='account')),
    path('', include('apps.public.urls', namespace='public')),
    path('program/', include('apps.program.urls', namespace='program')),
    path('exercise/', include('apps.exercise.urls', namespace='exercise')),
    path('package/', include('apps.package.urls', namespace='package')),
]

# Serve static files on dev
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
