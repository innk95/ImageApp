# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Image(models.Model):
    url = models.CharField(max_length=200, blank=True, default=None)
    file = models.ImageField(upload_to='images/', blank=True, default=None)



