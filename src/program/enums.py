from django.utils.translation import gettext as _
from django.db.models import TextChoices


# Day choices
class DayChoices(TextChoices):
    SATURDAY = '0', _('Saturday')
    SUNDAY = '1', _('Sunday')
    MONDAY = '2', _('Monday')
    TUESDAY = '3', _('Tuesday')
    WEDNESDAY = '4', _('Wednesday')
    THURSDAY = '5', _('Thursday')
    FRIDAY = '6', _('Friday')
