from django.utils.translation import gettext as _
from django.db import models


# Certificates model
class Certificate(models.Model):
    title = models.CharField(_('Certificate title'), max_length=64, null=True, blank=True, help_text=_('Optional'))
    picture = models.ImageField(_('Picture'), upload_to='images/certificates')

    class Meta:
        verbose_name = _('Certificate')
        verbose_name_plural = _('Certificates')
