from nested_admin import NestedStackedInline, NestedModelAdmin
from django.utils.translation import gettext as _
from django.shortcuts import redirect, reverse
from django.db import models as a_model
from django.contrib import admin
from django import forms
from . import models


# Diet Recommendations as inline
class DietRecommendInline(admin.TabularInline):
    model = models.DietRecommend
    extra = 1


# Diet MealFoods as inline
class MealFoodInline(NestedStackedInline):
    model = models.MealFood
    extra = 0
    readonly_fields = ('energy',)

    # Change formField attributes(size)
    formfield_overrides = {
        a_model.IntegerField: {"widget": forms.NumberInput(attrs={"size": "16"})},
        a_model.CharField: {"widget": forms.TextInput(attrs={"size": "20"})},
    }


# Register DailyDietMeal Model Admin
@admin.register(models.DailyDietMeal)
class DailyDietMealAdmin(NestedModelAdmin):
    readonly_fields = ('daily_program', 'meal')
    inlines = (MealFoodInline,)

    def has_module_permission(self, request):
        return False

    def response_add(self, request, obj, post_url_continue=None):
        """ Custom redirection after add obj """
        if "_save" in request.POST:
            return redirect(f'/admin/diet/dailydietprogram/{obj.daily_program.id}/change')

        # Call the parent class's response_add method for other actions
        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        """ Custom redirection after change obj """
        if "_save" in request.POST:
            return redirect(f'/admin/diet/dailydietprogram/{obj.daily_program.id}/change')

        # Call the parent class's response_change method for other actions
        return super().response_change(request, obj)

    def response_delete(self, request, obj_display, obj_id):
        return redirect('/admin/diet/dietprogram/')

    def get_view_on_site_url(self, obj=None):
        """ Custom redirection for "View on site" button """
        if obj:
            return reverse("diet:diet_program", args=(obj.daily_program.diet_program.id,))

        return reverse("account:users")


# DailyDietMeal as inline
class DailyDietMealInline(NestedStackedInline):
    model = models.DailyDietMeal
    inlines = (MealFoodInline,)
    extra = 0


# Register DailyDietProgram Model Admin
@admin.register(models.DailyDietProgram)
class DailyDietProgramAdmin(NestedModelAdmin):
    list_display = ('diet_program', 'get_user_diet_program_title',  'day')
    list_display_links = ('diet_program',)
    readonly_fields = ('diet_program', 'day')
    search_fields = ('diet_program__user__phonenumber', 'diet_program__user__last_name')
    list_filter = ('day',)
    inlines = (DailyDietMealInline,)

    def has_module_permission(self, request):
        return False

    def get_user_diet_program_title(self, obj):
        return obj.diet_program.title if obj.diet_program else None

    get_user_diet_program_title.short_description = _("Program Title")

    def response_add(self, request, obj, post_url_continue=None):
        """ Custom redirection after add obj """
        if "_save" in request.POST:
            return redirect(f'/admin/diet/dietprogram/{obj.diet_program.id}/change')

        # Call the parent class's response_add method for other actions
        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        """ Custom redirection after change obj """
        if "_save" in request.POST:
            return redirect(f'/admin/diet/dietprogram/{obj.diet_program.id}/change')

        # Call the parent class's response_change method for other actions
        return super().response_change(request, obj)

    def response_delete(self, request, obj_display, obj_id):
        return redirect('/admin/diet/dietprogram/')


# DailyDietProgram as inline
class DailyDietProgramInline(admin.TabularInline):
    model = models.DailyDietProgram
    extra = 0
    show_change_link = True


# Register DietProgram Model Admin
@admin.register(models.DietProgram)
class DietProgramAdmin(admin.ModelAdmin):
    list_display = ('get_user_phone', 'get_user_fullname', 'title')
    list_display_links = ('get_user_phone', 'get_user_fullname')
    search_fields = ('user__phonenumber', 'user__last_name')
    autocomplete_fields = ('user',)
    inlines = (DailyDietProgramInline, DietRecommendInline)

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


# Register Foods
@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'calories')
    list_display_links = ('title',)


# Register Meals
@admin.register(models.Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('title', 'time')
    list_display_links = ('title',)
