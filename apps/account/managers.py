from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _
from django.db import models


class CustomBaseUserManager(BaseUserManager):

    def create_user(self, phonenumber, password, email=None, **kwargs):
        """ Create and save a normal_user with the given phone number and password. """
        if not phonenumber:
            raise ValueError(_("The phone number must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, phonenumber=phonenumber, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_financial_user(self, phonenumber, password, email=None, **kwargs):
        return self.create_user(
            phonenumber=phonenumber, password=password, role='financial_user', email=email, **kwargs
        )

    def create_superuser(self, phonenumber, password, email=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            phonenumber=phonenumber, password=password, role='super_user', email=email, **kwargs
        )


class NormalUserManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(role='normal_user')


class SuperUserManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(role='super_user')
