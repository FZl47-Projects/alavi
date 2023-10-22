from django.utils.translation import gettext as _
from django.db import models as a_model
from django.contrib import admin
from django import forms
from .models import Package


# Package Model Admin
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('type', 'intcomma_price')
    list_display_links = ('type',)

    # Change formField attributes(size)
    formfield_overrides = {
        a_model.IntegerField: {"widget": forms.NumberInput(attrs={"size": "18"})},
    }

    def intcomma_price(self, obj):
        """ Return thousand seperated price. """
        if obj.price:
            return "{:,}".format(obj.price)

    intcomma_price.short_description = _('Price (Rials)')
