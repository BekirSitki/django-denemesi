from django.db import models

# Create your models here.

class Notlar(models.Model):
    baslik = models.CharField(max_length=30)
    icerik = models.CharField(max_length=255)