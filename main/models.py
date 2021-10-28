from django.db import models


# Create your models here.
class Motivasi(models.Model):
    to = models.CharField(max_length=10)
    pesan = models.CharField(max_length=200)
    