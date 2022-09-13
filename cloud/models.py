import uuid
from django.db import models
from django.forms import ModelForm
from taggit.managers import TaggableManager
from datetime import datetime

class Cabinet(models.Model):
    number = models.IntegerField(max_length=100)
    time = models.DateTimeField()
    state = models.IntegerField()
    alarm = models.IntegerField(max_length=1)
    temperature = models.IntegerField(max_length=100)
    humidity = models.IntegerField(max_length=100)
    pressure = models.IntegerField(max_length=1000)
    lux = models.IntegerField(max_length=5000)
    co2 = models.IntegerField(max_length=5000)
    co = models.IntegerField(max_length=5000)
    gas = models.IntegerField(max_length=5000)
    movement = models.IntegerField(max_length=1)
    door = models.IntegerField(max_length=1)




