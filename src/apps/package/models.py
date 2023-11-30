from django.utils.translation import gettext as _
from .enums import PackageChoices
from django.db import models


# Packages model
class Package(models.Model):
    PACKAGES = PackageChoices

    type = models.CharField(_('Package type'), max_length=128, choices=PACKAGES.choices, default=PACKAGES.DIET)
    price = models.IntegerField(_('Price'), default=0, help_text=_('Rials'))

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modify time'), auto_now=True)

    class Meta:
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')
        ordering = ('id',)

    @property
    def get_type_label(self):
        return self.get_type_display()

    def __str__(self) -> str:
        return f'{self.get_type_label} - {self.price}'
