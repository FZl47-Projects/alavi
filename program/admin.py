from django.contrib import admin
from .models import Food,Sport,Diet_program_object,Training_program_object, Diet_program_object_free

# Register your models here.

admin.site.register(Food)
admin.site.register(Sport)
admin.site.register(Diet_program_object)
admin.site.register(Diet_program_object_free)
admin.site.register(Training_program_object)