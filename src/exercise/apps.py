from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class ExerciseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exercise'
    verbose_name = _('Exercise')
