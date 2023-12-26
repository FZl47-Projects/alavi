from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db import models

from apps.package.models import Package

User = get_user_model()


# PurchaseRequests class
class PurchaseRequest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='purchase_request')
    package = models.ManyToManyField(Package, verbose_name=_('packages'), related_name='purchase_requests')

    class Meta:
        verbose_name = _('Purchase request')
        verbose_name_plural = _('Purchase requests')

    def __str__(self):
        return f'{self.user}'
