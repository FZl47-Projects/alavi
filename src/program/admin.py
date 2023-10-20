from nested_admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
from django.utils.translation import gettext as _
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
        a_model.CharField: {"widget": forms.TextInput(attrs={"size": "17"})},
    }


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
