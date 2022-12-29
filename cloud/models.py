import uuid
from django.db import models
from django.forms import ModelForm
from taggit.managers import TaggableManager
from datetime import datetime

class Cabinet(models.Model):
    number = models.CharField(max_length=100, default=0)
    time = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default=0)
    alarm = models.CharField(max_length=100, default=0)
    temperature = models.CharField(max_length=100, default=0)
    humidity = models.CharField(max_length=100, default=0)
    pressure = models.CharField(max_length=100, default=0)
    lux = models.CharField(max_length=100, default=0)
    co2 = models.CharField(max_length=100, default=0)
    co = models.CharField(max_length=100, default=0)
    gas = models.CharField(max_length=100, default=0)
    movement = models.CharField(max_length=100, default=0)
    door = models.CharField(max_length=100, default=0)




