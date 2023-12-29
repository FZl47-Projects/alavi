from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from apps.package.models import Package
from . import managers
import secrets


class User(AbstractUser):
    ROLE_USER_OPTIONS = (
        ('normal_user', _('normal_user')),
        ('super_user', _('super_user')),
    )

    username = None
    email = models.EmailField(_("Email address"), null=True, blank=True, unique=False)
    phonenumber = PhoneNumberField(verbose_name=_('Phone number'), region='IR', unique=True)
    role = models.CharField(_('User role'), max_length=20, choices=ROLE_USER_OPTIONS, default='normal_user')
    packages = models.ManyToManyField(Package, verbose_name=_('Packages'), related_name='users', blank=True)

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = []

    objects = managers.CustomBaseUserManager()
    normal_user = managers.NormalUserManager()
    super_user = managers.SuperUserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = '-id',

    def __str__(self):
        return f'{self.get_full_name()} - {self.get_raw_phonenumber()}'

    @property
    def is_normal_user(self):
        return True if self.role in settings.USER_ROLES else False

    @property
    def is_admin_user(self):
        return True if self.role in settings.ADMIN_USER_ROLES else False

    def get_raw_phonenumber(self):
        p = str(self.phonenumber).replace('+98', '')
        return p

    get_raw_phonenumber.short_description = _('Phone number')

    def get_full_name(self):
        fl = f'{self.first_name} {self.last_name}'.strip() or 'بدون نام'
        return fl

    def get_email(self):
        return self.email

    def get_image_url(self):
        try:
            return self.user_profile.picture.url
        except (AttributeError, ValueError):
            return '/static/front/images/userimage.png'

    def get_last_login(self):
        if self.last_login:
            return self.last_login.strftime('%Y-%m-%d %H:%M:%S')
        return '-'

    def get_absolute_url(self):
        if self.is_normal_user:
            return reverse('account:user-profile', args=(self.id,))
        else:
            return reverse('account:home-admin')

    def get_diet_programs(self):
        return self.diet_programs.all()

    def get_exercise_programs(self):
        return self.exercise_programs.all()

    def get_model_fields(self):
        return self._meta.get_fields()

    def has_package(self, package_name):
        for package in self.packages.all():
            if package_name == package.type or package_name in package.type:
                return True
        return False


# ExerciseDays model
class ExerciseDay(models.Model):
    name = models.CharField(_('Day of week'), max_length=16)

    class Meta:
        verbose_name = _('Exercise day')
        verbose_name_plural = _('Exercise days')
        ordering = ('id',)

    def __str__(self) -> str:
        return self.name


# UserProfiles models
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='user_profile')
    token = models.CharField(_("Profile token"), max_length=64, null=True, blank=True)

    picture = models.ImageField(_('User picture'), null=True, blank=True, upload_to='images/%Y/%m/%d/users')
    national_code = models.PositiveIntegerField(_('National code'), null=True, blank=True, default=0)

    # Body info
    weight = models.PositiveIntegerField(_('Weight'), default=0, help_text=_('Kg'))
    height = models.PositiveIntegerField(_('Height'), default=0, help_text=_('cm'))
    waist_size = models.PositiveIntegerField(_('Waist size'), null=True, blank=True, default=0, help_text=_('cm'))
    hip_size = models.PositiveIntegerField(_('Hip size'), null=True, blank=True, default=0, help_text=_('cm'))
    arm_size = models.PositiveIntegerField(_('Arm size'), null=True, blank=True, default=0, help_text=_('cm'))
    chest_size = models.PositiveIntegerField(_('Chest size'), null=True, blank=True, default=0, help_text=_('cm'))

    # Exercise info
    physical_damage = models.BooleanField(_('Physical damage'), default=False)
    damage_type = models.CharField(_('Damage type/area'), max_length=128, null=True, blank=True)
    regular_exercise = models.BooleanField(_('Regular/Pro exercise'), default=False)
    exercise_name = models.CharField(_('Exercise name'), max_length=128, null=True, blank=True)
    doing_exercise = models.CharField(_('Doing exercise'), max_length=64, default=_('I do not exercise'))  # Should be choices (3 choices)
    exercise_days = models.ManyToManyField(ExerciseDay, verbose_name=_('Exercise days willing'), blank=True, related_name='user_profile')

    # Survey
    last_exercise = models.TextField(_('Last time exercise'), null=True, blank=True)
    goal_of_program = models.TextField(_('Goal of getting program'), null=True, blank=True)
    exercise_systems = models.TextField(_('Exercise system experience'), null=True, blank=True)
    additional_explain = models.TextField(_('Additional explanations'), null=True, blank=True)

    # Disease history
    family_disease = models.BooleanField(_('Family disease history'), default=False)
    family_disease_name = models.CharField(_('Family disease name'), max_length=128, null=True, blank=True)
    special_disease = models.BooleanField(_('Special disease'), default=False)
    special_disease_name = models.CharField(_('Special disease name'), max_length=128, null=True, blank=True)
    special_medicine = models.BooleanField(_('Special medicine'), default=False)
    medicine_name = models.CharField(_('Special medicine name'), max_length=128, null=True, blank=True)

    # Food/Supplement info
    breakfast_time = models.CharField(_('Breakfast time willing'), max_length=8, default='-')  # Between (06:00 - 10:00)
    am_snack_time = models.CharField(_('AM Snack time willing'), max_length=8, default='-')  # Between (10:00 - 12:00)
    launch_time = models.CharField(_('Launch time willing'), max_length=8, default='-')  # Between (12:30 - 17:00)
    pm_snack_time = models.CharField(_('PM Snack time willing'), max_length=8, default='-')
    dinner_time = models.CharField(_('Dinner time willing'), max_length=8, default='-')  # Between (18:30 - 21:30)

    use_supplement = models.BooleanField(_('Use supplement'), default=False)
    supplement_name = models.CharField(_('Supplement name'), max_length=128, null=True, blank=True)
    want_supplement = models.BooleanField(_('Want supplement'), default=False)
    used_steroids = models.BooleanField(_('Used steroids'), default=False)
    steroids_name = models.CharField(_('Steroid medicine name'), max_length=128, null=True, blank=True)
    in_diet = models.BooleanField(_('Had/Has diet'), default=False)
    diet_name = models.CharField(_('Diet name'), max_length=128, null=True, blank=True)
    vegetarian = models.BooleanField(_('Vegetarian'), default=False)

    # Documents
    body_composition = models.FileField(_('Body composition'), null=True, blank=True, upload_to='images/users/docs')
    body_checkup = models.FileField(_('Body checkup'), null=True, blank=True, upload_to='images/users/docs')
    body_picture = models.FileField(_('Body picture'), null=True, blank=True, upload_to='images/users/docs')

    verified = models.BooleanField(_('Verified'), default=False)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modify time'), auto_now=True)

    class Meta:
        verbose_name = _('User profile')
        verbose_name_plural = _('User profiles')
        ordering = ('-id',)

    def generate_token(self, byte: int = 12):
        self.token = secrets.token_hex(byte)
        self.save()

    def clear_token(self, request):
        if 'register_token' in request.session:
            del request.session['register_token']

        self.token = None
        self.save()

    def __str__(self) -> str:
        return f'{self.user}'
