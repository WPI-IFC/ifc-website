from datetime import datetime

from django.db import models
from django.conf import settings

from houses.models import Fraternity

class BaseEvent(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    splash_img = models.ImageField(upload_to='event_splash/')

    @property
    def d_time_start(self):
        return datetime.combine(self.date, self.start_time)
    
    @property
    def d_time_end(self):
        return datetime.combine(self.date, self.end_time)

    def __str__(self):
        return "{} - {}, {}-{}".format(
            self.title,
            self.date,
            self.start_time,
            self.end_time
        )

    class Meta:
        abstract = True
        ordering = ("-date", "-start_time",)

class OfficerEvent(BaseEvent):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )


class HouseEvent(BaseEvent):
    owner = models.ForeignKey(
        Fraternity,
        on_delete=models.CASCADE
    )