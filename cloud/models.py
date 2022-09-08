import uuid
from django.db import models
from django.forms import ModelForm
from taggit.managers import TaggableManager
from datetime import datetime

class Cabinet(models.Model):
    number = models.IntegerField()
    subject = models.CharField(max_length=100)
    sensors = models.CharField(max_length=100)

