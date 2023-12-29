from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib import admin

from django_q.models import Failure, OrmQ, Schedule, Success


# Unregister groups
admin.site.unregister(Group)


# Unregister django-q models
# admin.site.unregister(Failure)
# admin.site.unregister(OrmQ)
# admin.site.unregister(Schedule)
# admin.site.unregister(Success)


# Rename admin site header & title & index_title
admin.site.site_header = _("Alavi sport club")
admin.site.index_title = _("Management panel")
admin.site.site_title = _("Alavi gym")
