from django.utils.translation import gettext as _
from django.db.models import TextChoices


# Workout levels
class WorkoutLevelChoices(TextChoices):
    EASY = '0', _('Easy')
    NORMAL = '1', _('Normal')
    HARD = '2', _('Hard')


# Weeks
class WeekChoices(TextChoices):
    FIRST = '0', _('First week')
    SECOND = '1', _('Second week')
    THIRD = '2', _('Third week')
    FOURTH = '3', _('Fourth week')
