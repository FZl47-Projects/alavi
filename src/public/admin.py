from nested_admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
from django.shortcuts import redirect, reverse
from django.db import models as a_model
from django.contrib import admin
from django import forms
from . import models


# Free Exercise as inline
class FreeExerciseInline(NestedStackedInline):
    model = models.FreeExercise
    extra = 0

    # Change formField attributes(size)
    formfield_overrides = {
        a_model.CharField: {"widget": forms.TextInput(attrs={"size": "17"})},
    }


# FreeDailyExercise Model Admin
@admin.register(models.FreeDailyExercise)
class FreeDailyExerciseAdmin(admin.ModelAdmin):
    inlines = (FreeExerciseInline,)


# FreeDailyExercise as inline
class FreeDailyExerciseInline(NestedStackedInline):
    model = models.FreeDailyExercise
    inlines = (FreeExerciseInline,)
    extra = 0


# Register FreeWeeklyExercise Model Admin
@admin.register(models.FreeWeeklyExercise)
class FreeWeeklyExerciseAdmin(NestedModelAdmin):
    list_display = ('exercise_program', 'week')
    list_display_links = ('exercise_program',)
    readonly_fields = ('exercise_program', 'week')
    inlines = (FreeDailyExerciseInline,)

    def has_module_permission(self, request):
        return False

    def response_add(self, request, obj, post_url_continue=None):
        """ Custom redirection after add obj """
        if "_save" in request.POST:
            return redirect(f'/admin/public/freeweeklyexercise/{obj.exercise_program.id}/change')

        # Call the parent class's response_add method for other actions
        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        """ Custom redirection after change obj """
        if "_save" in request.POST:
            return redirect(f'/admin/public/freeweeklyexercise/{obj.exercise_program.id}/change')

        # Call the parent class's response_change method for other actions
        return super().response_change(request, obj)

    def response_delete(self, request, obj_display, obj_id):
        return redirect('/admin/public/freeweeklyexercise/')


# FreeWeeklyExercise as inline
class FreeWeeklyExerciseInline(admin.TabularInline):
    model = models.FreeWeeklyExercise
    extra = 0
    max_num = 4
    show_change_link = True


# Register FreeExerciseProgram Model Admin
@admin.register(models.FreeExerciseProgram)
class FreeExerciseProgramAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_active')
    list_display_links = ('__str__',)
    inlines = (FreeWeeklyExerciseInline,)

    def get_view_on_site_url(self, obj=None):
        """ Custom redirection for "View on site" button """
        if obj:
            return reverse('public:free_exercise')
        
        return super().get_view_on_site_url(obj)


admin.site.register(models.Certificate)
