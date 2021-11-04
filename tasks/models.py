from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) # Delete profile when user is deleted
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 30)
    task_date = models.DateField()
    end_time = models.TimeField()
    
    
    
    
