import uuid
from django.db import models
from django.forms import ModelForm
from taggit.managers import TaggableManager
from datetime import datetime

class Cabinet(models.Model):
    number = models.IntegerField(default=0)
    time = models.DateTimeField(default='')
    state = models.IntegerField(default=0)
    alarm = models.IntegerField(default=0)
    temperature = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    pressure = models.IntegerField(default=0)
    lux = models.IntegerField(default=0)
    co2 = models.IntegerField(default=0)
    co = models.IntegerField(default=0)
    gas = models.IntegerField(default=0)
    movement = models.IntegerField(default=0)
    door = models.IntegerField(default=0)




