from django.utils.translation import gettext as _
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class CustomBaseUserManager(BaseUserManager):

    def create_user(self, phonenumber, password, email=None, **extra_fields):
        """
        Create and save a normal_user with the given phonenumber and password.
        """
        if not phonenumber:
            raise ValueError(_("The phonenumber must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, phonenumber=phonenumber, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_financial_user(self, phonenumber, password, email=None, **extra_fields):
        return self.create_user(phonenumber=phonenumber, password=password, role='financial_user', email=email,
                                **extra_fields)

    def create_superuser(self, phonenumber, password, email=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(phonenumber=phonenumber, password=password, role='super_user', email=email,
                                **extra_fields)


class NormalUserManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(role='normal_user')


class SuperUserManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(role='super_user')


class User(AbstractUser):
    ROLE_USER_OPTIONS = (
        ('normal_user', _('normal_user')),
        ('super_user', _('super_user')),
    )

    username = None
    email = models.EmailField(_("Email address"), null=True, blank=True, unique=False)
    phonenumber = PhoneNumberField(verbose_name=_('Phone number'), region='IR', unique=True)
    # type users|roles
    role = models.CharField(_('User role'), max_length=20, choices=ROLE_USER_OPTIONS, default='normal_user')

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = []

    objects = CustomBaseUserManager()
    normal_user = NormalUserManager()
    super_user = SuperUserManager()

    class Meta:
        ordering = '-id',

    def __str__(self):
        return f'{self.role} - {self.phonenumber}'

    @property
    def is_normal_user(self):
        return True if self.role in settings.USER_ROLES else False

    @property
    def is_admin_user(self):
        return True if self.role in settings.ADMIN_USER_ROLES else False

    def get_raw_phonenumber(self):
        p = str(self.phonenumber).replace('+98', '')
        return p

    def get_full_name(self):
        fl = f'{self.first_name} {self.last_name}'.strip() or 'بدون نام'
        return fl

    def get_email(self):
        return self.email

    def get_image_url(self):
        try:
            return self.info.picture.url
        except AttributeError:
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

    def get_training_programs(self):
        return self.user_training_program.all()


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info')
    picture = models.ImageField(upload_to='images/%Y/%m/%d/users')
    national_code = models.PositiveIntegerField("height", default=0)
    height = models.PositiveIntegerField("height", default=0)
    weight = models.PositiveIntegerField("weight", default=0)
