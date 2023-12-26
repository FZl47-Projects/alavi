from django.db import models as a_model
from django.contrib import admin
from django import forms
from . import models


# FreeContents model admin
@admin.register(models.FreeContent)
class FreeContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')
    list_display_links = ('title',)

    # Change formField attributes(size)
    formfield_overrides = {
        a_model.CharField: {"widget": forms.TextInput(attrs={"size": "80"})},
    }


admin.site.register(models.Certificate)
