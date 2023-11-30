from django.utils.translation import gettext as _
from django.db.models import TextChoices


# Package choices
class PackageChoices(TextChoices):
    DIET = 'diet', _('Diet')
    WORKOUT = 'workout', _('workout')
    CROSSFIT = 'crossfit', _('Crossfit')
    WORKOUT_DIET = 'workout_diet', _('Workout + Diet')
    CROSSFIT_DIET = 'crossfit_diet', _('Crossfit + Diet')
    ANY_DIET = 'any_diet', _('Any sport + Diet')
    OFFLINE = 'offline', _('Offline')
