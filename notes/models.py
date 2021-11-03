from django.db import models

# Create your models here.
class notes(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    message = models.TextField(default='', blank = True)