from django.db import models

# Create your models here.
class notes(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date_created = models.DateField(null=True)
    message = models.TextField(default='', blank = True)
