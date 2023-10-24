from nested_admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
from django.shortcuts import redirect, reverse
from django.db import models as a_model
from django.contrib import admin
from django import forms
from . import models


# Free Diet MealFoods as inline
class FreeMealFoodInline(NestedStackedInline):
    model = models.FreeMealFood
    extra = 0
    readonly_fields = ('energy',)

    # Change formField attributes(size)
    formfield_overrides = {
        a_model.CharField: {"widget": forms.TextInput(attrs={"size": "17"})},
    }


# DailyDietMeal as inline
class FreeDailyDietMealInline(NestedStackedInline):
    model = models.FreeDietMeal
    inlines = (FreeMealFoodInline,)
    extra = 0


# Register FreeDailyDietProgram Model Admin
@admin.register(models.FreeDailyDietProgram)
class FreeDailyDietProgramAdmin(NestedModelAdmin):
    list_display = ('diet_program', 'day')
    list_display_links = ('diet_program',)
    readonly_fields = ('diet_program', 'day')
    inlines = (FreeDailyDietMealInline,)

    def has_module_permission(self, request):
        return False

    def response_add(self, request, obj, post_url_continue=None):
        """ Custom redirection after add obj """
        if "_save" in request.POST:
            return redirect(f'/admin/public/freedietprogram/{obj.diet_program.id}/change')

        # Call the parent class's response_add method for other actions
        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        """ Custom redirection after change obj """
        if "_save" in request.POST:
            return redirect(f'/admin/public/freedietprogram/{obj.diet_program.id}/change')

        # Call the parent class's response_change method for other actions
        return super().response_change(request, obj)

    def response_delete(self, request, obj_display, obj_id):
        return redirect('/admin/public/freedietprogram/')


# DailyDietProgram as inline
class FreeDailyDietProgramInline(admin.TabularInline):
    model = models.FreeDailyDietProgram
    extra = 0
    show_change_link = True


# Register FreeDietProgram Model Admin
@admin.register(models.FreeDietProgram)
class FreeDietProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active')
    list_display_links = ('id',)
    inlines = (FreeDailyDietProgramInline,)

    def get_view_on_site_url(self, obj=None):
        """ Custom redirection for "View on site" button """
        if obj:
            return reverse('public:free_diet')
        
        return super().get_view_on_site_url(obj)


admin.site.register(models.Certificate)
