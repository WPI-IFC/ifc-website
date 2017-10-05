from django.db import models

class Fraternity(models.Model):
    english_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, blank=True)
    letters = models.ImageField(
        upload_to="letters"
        )
    pimary_color = models.CharField(max_length=7)
    secondary_color = models.CharField(max_length=7)
    featured_picture = models.ImageField(
        upload_to="featured",
        blank=True)
    values = models.TextField(blank=True)
    extra_info = models.TextField(blank=True)
    house_pic = models.ImageField(
        upload_to="house",
        blank=True)

    def __str__(self):
        return self.english_name

    def lower_repr(self):
        return ''.join(x for x in self.__str__().lower() if x != " ")

    class Meta:
        verbose_name_plural = "fraternities"