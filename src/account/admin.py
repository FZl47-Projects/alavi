from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = User

    list_display = ('get_raw_phonenumber', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'role')
    search_fields = ('email', 'phonenumber')
    ordering = ('email', 'phonenumber')
    fieldsets = (
        (None, {'fields': ('phonenumber', 'email', 'first_name', 'last_name', 'role')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions')}),
        (_('Dates'), {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phonenumber', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    
    def has_change_permission(self, request, obj=None):
        """ Prevent staff users from changing super_users obj. """
        if obj is not None and request.user.is_staff and obj.is_superuser:
            return False
        
        return super().has_change_permission(request, obj)

    def get_readonly_fields(self, request, obj=None):
        """ Prevent staff users to change some fields. """
        if request.user.is_superuser:
            return []

        fields = obj.get_model_fields()
        excludes = ['first_name', 'last_name']

        return [field.name for field in fields if field.name not in excludes]
