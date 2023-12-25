from nested_admin import NestedStackedInline, NestedModelAdmin
from django.shortcuts import redirect, reverse
from django.contrib import admin
from . import models


# FreeContents model admin


admin.site.register(models.Certificate)
