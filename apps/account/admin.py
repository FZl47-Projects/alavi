from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin
from django.utils.html import escape, mark_safe
from django.shortcuts import reverse
from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, UserProfile, ExerciseDay
from apps.order.models import PurchaseRequest


# Register PurchaseRequest as Inline
class PurchaseRequestInline(admin.StackedInline):
    model = PurchaseRequest
    readonly_fields = ('package',)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = User

    list_display = ('get_raw_phonenumber', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'profile_link')
    list_filter = ('is_active', 'is_staff', 'role')
    date_hierarchy = 'date_joined'
    search_fields = ('email', 'phonenumber', 'last_name')
    ordering = ('phonenumber', 'email')
    filter_horizontal = ('packages', 'user_permissions')
    inlines = (PurchaseRequestInline,)

    fieldsets = (
        (None, {'fields': ('phonenumber', 'email', 'first_name', 'last_name', 'role')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions')}),
        (_('Dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Packages'), {'fields': ('packages',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phonenumber', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    
    def has_change_permission(self, request, obj=None):
        """ Prevent staff users from changing super_users obj. """
        if obj is not None and not request.user.is_superuser and obj.is_superuser:
            return False
        
        return super().has_change_permission(request, obj)

    def get_readonly_fields(self, request, obj=None):
        """ Prevent staff users to change some fields. """
        if request.user.is_superuser:
            return []

        fields = obj.get_model_fields()
        excludes = ['packages']

        return [field.name for field in fields if field.name not in excludes]

    @admin.display(description=_('Profile'))
    def profile_link(self, obj):
        link = reverse("admin:account_userprofile_change", args=[obj.user_profile.id])
        return mark_safe(f'<a href="{link}">{escape(_("View"))}</a>')

    profile_link.allow_tags = True


# UserProfile Model Admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'national_code', 'verified')
    list_display_links = ('user',)
    readonly_fields = ('national_code', 'created_at', 'modified_at')
    list_filter = ('verified',)
    search_fields = ('user__phonenumber', 'user__last_name')

    fieldsets = (
        (None, {'fields': ('user', 'national_code', 'picture')}),
        (_('Survey'), {'fields': ('last_exercise', 'goal_of_program', 'exercise_systems', 'additional_explain')}),
        (_('Body info'), {'fields': ('weight', 'height', 'waist_size', 'hip_size', 'arm_size', 'chest_size')}),
        (_('Disease history'), {'fields': ('family_disease', 'family_disease_name', 'special_disease', 'special_disease_name', 'special_medicine', 'medicine_name')}),
        (_('Food/Supplement info'), {'fields': ('breakfast_time', 'am_snack_time', 'launch_time', 'pm_snack_time', 'dinner_time')}),
        (_('Continue food info'), {'fields': ('use_supplement', 'supplement_name', 'want_supplement', 'used_steroids', 'steroids_name', 'in_diet', 'diet_name', 'vegetarian')}),
        (_('Exercise info'), {'fields': ('physical_damage', 'regular_exercise', 'exercise_name', 'doing_exercise', 'exercise_days')}),
        (_('Documents'), {'fields': ('body_composition', 'body_checkup', 'body_picture')}),
        (_('Important dates'), {'fields': ('created_at', 'modified_at')}),
        (_('Verification'), {'fields': ('verified',)}),
    )

    def get_view_on_site_url(self, obj=None):
        if obj:
            return reverse('account:user-profile', args=(obj.id,))


admin.site.register(ExerciseDay)
