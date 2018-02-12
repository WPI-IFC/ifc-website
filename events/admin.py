from django.contrib import admin

from . import models

admin.site.register(models.OfficerEvent)
admin.site.register(models.HouseEvent)