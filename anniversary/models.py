from django.db import models

# Create your models here.
class Anniversary(models.Model):
    datetime = models.DateTimeField('Date')
    url = models.URLField('Video URL', blank=False)
    location = models.CharField('Location', max_length=255)
    name = models.CharField('Name', max_length=255)

    class Meta:
        ordering = ('-datetime',)