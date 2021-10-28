from django.db import models

# Create your models here.
class to_do_list(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    due_date = models.DateField()
    description = models.CharField(max_length=30)