from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class PackageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.package'
    verbose_name = _('Package')
