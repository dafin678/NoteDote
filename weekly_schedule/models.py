from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Weekly_schedule(models.Model):
    DAY_CHOICES = (
        (1,'monday'),
        (2,'tuesday'),
        (3,'wednesday'),
        (4,'thursday'),
        (5,'friday'),
        (6,'saturday'),
        (7,'sunday')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    day = models.IntegerField(choices=DAY_CHOICES, default=0)
    start_time = models.TimeField(null=True)
    due_time = models.TimeField(null=True)