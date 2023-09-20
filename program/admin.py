from django.contrib import admin
from .models import Day,Food,Sport,Diet_program_object,Training_program_object

# Register your models here.

admin.site.register(Day)
admin.site.register(Food)
admin.site.register(Sport)
admin.site.register(Diet_program_object)
admin.site.register(Training_program_object)