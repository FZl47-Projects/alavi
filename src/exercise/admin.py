from nested_admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
from django.utils.translation import gettext as _
from django.shortcuts import reverse, redirect
from django.db import models as a_model
from django.contrib import admin
from django import forms
from . import models


# ExerciseInline as inline
class ExerciseInline(NestedStackedInline):
    model = models.Exercise
    extra = 0


# DailyExerciseProgram as inline
class DailyExerciseProgramInline(NestedStackedInline):
    model = models.DailyExerciseProgram
    extra = 0
    inlines = (ExerciseInline,)

    # Change formField attributes(size)
    formfield_overrides = {
        a_model.CharField: {"widget": forms.TextInput(attrs={"size": "18"})},
    }


# Register WeeklyExerciseProgram Model Admin
@admin.register(models.WeeklyExerciseProgram)
class WeeklyExerciseProgramAdmin(NestedModelAdmin):
    readonly_fields = ('exercise_program', 'week')
    search_fields = ('exercise_program__user__phonenumber', 'exercise_program__user__last_name')
    list_filter = ('week',)
    fields = ('exercise_program', 'week', 'warm_up', 'cool_down')
    inlines = (DailyExerciseProgramInline,)

    def has_module_permission(self, request):
        return False

    def response_add(self, request, obj, post_url_continue=None):
        """ Custom redirection after add obj """
        if "_save" in request.POST:
            return redirect(f'/admin/exercise/exerciseprogram/{obj.exercise_program.id}/change')

        # Call the parent class's response_add method for other actions
        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        """ Custom redirection after change obj """
        if "_save" in request.POST:
            return redirect(f'/admin/exercise/exerciseprogram/{obj.exercise_program.id}/change')

        # Call the parent class's response_change method for other actions
        return super().response_change(request, obj)


# WeeklyExerciseProgram as inline
class WeeklyExerciseProgramInline(admin.TabularInline):
    model = models.WeeklyExerciseProgram
    fields = ('week',)
    extra = 0
    show_change_link = True


# Register ExerciseProgram Model Admin
@admin.register(models.ExerciseProgram)
class ExerciseProgramAdmin(admin.ModelAdmin):
    list_display = ('get_user_phone', 'get_user_fullname', 'title')
    list_display_links = ('get_user_phone', 'get_user_fullname')
    search_fields = ('user__phonenumber', 'user__last_name')
    autocomplete_fields = ('user',)
    inlines = (WeeklyExerciseProgramInline,)

    def get_user_phone(self, obj):
        return obj.user.get_raw_phonenumber() if obj.user else None

    def get_user_fullname(self, obj):
        return obj.user.get_full_name() if obj.user else None

    get_user_phone.short_description = _("User phone")
    get_user_fullname.short_description = _("User name")

    def get_view_on_site_url(self, obj=None):
        """ Custom redirection for "View on site" button """
        if obj:
            return reverse("account:user-profile", args=(obj.user.id,))

        return reverse("account:users")


# Register Workout
@admin.register(models.Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'level')
    list_display_links = ('title',)
