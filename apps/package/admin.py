from django.utils.translation import gettext as _
from django.db import models as a_model
from django.contrib import admin
from django import forms
from .models import Package, PackageInfo


# Package info Model Admin as Inline
class PackageInfoInline(admin.TabularInline):
    model = PackageInfo
    extra = 0

    # Change formField attributes(size)
    formfield_overrides = {
        a_model.CharField: {"widget": forms.TextInput(attrs={"size": "100"})},
    }


# Package Model Admin
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('type', 'intcomma_price')
    list_display_links = ('type',)
    inlines = (PackageInfoInline,)

    # Change formField attributes(size)
    formfield_overrides = {
        a_model.IntegerField: {"widget": forms.NumberInput(attrs={"size": "18"})},
    }

    @admin.display(description=_('Price (Rials)'))
    def intcomma_price(self, obj):
        """ Return thousand seperated price. """
        if obj.price:
            return "{:,}".format(obj.price)
