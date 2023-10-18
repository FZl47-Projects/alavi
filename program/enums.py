from django.db.models import TextChoices


# Day choices
class Days(TextChoices):
    SATURDAY = '0', 'شنبه'
    SUNDAY = '1', 'یکشنبه'
    MONDAY = '2', 'دوشنبه'
    TUESDAY = '3', 'سه شنبه'
    WEDNESDAY = '4', 'چهارشنبه'
    THURSDAY = '5', 'پنجشنبه'
    FRIDAY = '6', 'جمعه'
