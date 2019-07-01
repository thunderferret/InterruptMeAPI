from __future__ import unicode_literals
from django.db import models


# Create your models here.

class User(models.Model):
    uid = models.CharField('uid', max_length=30)
    interval = models.IntegerField('interval')
    start_time = models.DateTimeField('start_time')
    end_time = models.DateTimeField('end_time')
    isActive = models.BooleanField('isactive')
