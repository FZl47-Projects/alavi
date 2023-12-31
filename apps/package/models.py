from django.utils.translation import gettext as _
from .enums import PackageChoices
from django.db import models


# Packages model
class Package(models.Model):
    PACKAGES = PackageChoices

    type = models.CharField(_('Package type'), max_length=128, choices=PACKAGES.choices, default=PACKAGES.DIET)
    price = models.IntegerField(_('Price'), default=0, help_text=_('Rials'))
    buy_link = models.URLField(_('Purchase link'), null=True, blank=True)
    icon = models.ImageField(_('Package icon'), upload_to='images/packages/icons', null=True, blank=True)
    fw_class = models.CharField(_('FontAwesome css class'), max_length=64, null=True, blank=True)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modify time'), auto_now=True)

    class Meta:
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')
        ordering = ('id',)

    @property
    def get_type_label(self):
        return self.get_type_display()

    def get_package_info(self):
        return self.package_info.all()

    def __str__(self) -> str:
        return f'{self.get_type_label} - {self.price}'


# PackageInfo model
class PackageInfo(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, verbose_name=_('Package'), related_name='package_info')
    text = models.CharField(_('Text'), max_length=255)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modify time'), auto_now=True)

    class Meta:
        verbose_name = _('Package info')
        verbose_name_plural = _('Package infos')
