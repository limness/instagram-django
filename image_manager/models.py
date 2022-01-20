from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='site_media')

class Description(models.Model):
    description = models.CharField(default='', max_length=200)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
