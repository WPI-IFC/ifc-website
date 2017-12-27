from django.db import models
from django.conf import settings

class Biography(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    headshot = models.ImageField()

    class Meta():
        verbose_name_plural = "bibliographies"

class Blog(models.Model):
    current_owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT, # We need to transfer ownership
                                  # before we delete a user
                                  # since these belong to positions not users
    )
    position_title = models.CharField(max_length=100)



class Post(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
    )
    published = models.DateField()
    last_edit = models.DateTimeField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    author_string = models.CharField(max_length=100) # In case users ever do get deleted
                                                     # this provides some backup
    title = models.CharField(max_length=100)
    body = models.TextField()
    attachments = models.FileField()

    class Meta():
        ordering = ("published",)