from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Weekly_schedule(models.Model):
    name = models.CharField(max_length=30)
    day = models.CharField(max_length=15)
    start_time = models.TimeField()
    due_time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')