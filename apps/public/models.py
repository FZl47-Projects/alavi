from django.utils.translation import gettext as _
from django.db import models
from ckeditor.fields import RichTextField


# Certificates model
class Certificate(models.Model):
    title = models.CharField(_('Certificate title'), max_length=64, null=True, blank=True, help_text=_('Optional'))
    picture = models.ImageField(_('Picture'), upload_to='images/certificates')

    class Meta:
        verbose_name = _('Certificate')
        verbose_name_plural = _('Certificates')


# FreeContents model
class FreeContent(models.Model):
    title = models.CharField(_('Content title'), max_length=64, default=_('No title'))
    short_description = models.CharField(_('Short description'), max_length=64, help_text=_('Date, extra info, ...'))
    text = RichTextField(verbose_name=_('Text'))

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modify time'), auto_now=True)

    class Meta:
        verbose_name = _('Free content')
        verbose_name_plural = _('Free contents')
        ordering = ('-id',)

    def __str__(self):
        return f'{self.title}, {self.short_description[:15]}'
