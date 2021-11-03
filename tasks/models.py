from django.db import models

class Task(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 30)
    task_date = models.DateField()
    end_time = models.TimeField()
    
    
    
    
