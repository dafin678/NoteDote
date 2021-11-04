from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Weekly_schedule(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) # Delete profile when user is deleted
    name = models.CharField(max_length=30)
    day = models.CharField(max_length=15)
    start_time = models.TimeField(null=True)
    due_time = models.TimeField(null=True)
    