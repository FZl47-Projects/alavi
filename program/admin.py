from django.contrib import admin
from .models import Food, Sport, DietProgram, TrainingProgram, DietProgramFree


admin.site.register(Food)
admin.site.register(Sport)
admin.site.register(DietProgram)
admin.site.register(DietProgramFree)
admin.site.register(TrainingProgram)
