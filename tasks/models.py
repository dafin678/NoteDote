from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 30)
    task_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)
    
    
    
    
