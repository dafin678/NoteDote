from django.db import models

# Create your models here.
class weekly_schedule(models.Model):
    name = models.CharField(max_length=30)
    day = models.CharField(max_length=15)
    start_time = models.DateTimeField()

