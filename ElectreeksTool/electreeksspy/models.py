"""
Electreeks® SpyAgent
An App based on a Django framework

© Electreeks® - Hans Umlauft
"""

from django.db import models

# Create your models here.

class Stream(models.Model):
    name = models.CharField(max_length=200)
    streaming_url = models.CharField(max_length=200)
    def __str__(self):
        return self.name
        return self.streaming_url
