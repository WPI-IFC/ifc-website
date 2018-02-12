from django.db import models
from django.conf import settings

from houses.models import Fraternity

class BaseEvent(models.Model):
    title = models.CharField(max_length=100)
    d_time = models.DateTimeField()
    description = models.TextField()
    splash_img = models.ImageField(upload_to='event_splash/')

    def __str__(self):
        return self.title + " - " + str(self.d_time)

    class Meta:
        abstract = True

class OfficerEvent(BaseEvent):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )


class HouseEvent(BaseEvent):
    owner = models.ForeignKey(
        Fraternity,
        on_delete=models.CASCADE
    )