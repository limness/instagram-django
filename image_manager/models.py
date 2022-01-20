
from django.db import models

import os


class Image(models.Model):
    image = models.ImageField(upload_to='site_media')

    def filename(self):
        return '/m/site_media/' + os.path.basename(self.image.name)

class Description(models.Model):
    description = models.CharField(default='', max_length=200)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
