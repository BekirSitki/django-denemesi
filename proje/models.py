import django
from django.db import models
from datetime import date
from django import utils
# Create your models here.

class Notlar(models.Model):
    baslik = models.CharField(max_length=30)
    icerik = models.CharField(max_length=255)
    tarih  = models.DateField(default=django.utils.timezone.now)