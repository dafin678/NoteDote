from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from .models import Task

@receiver(post_save, sender=User) 
def create_task(sender, instance, created, **kwargs):
    if created:
        Task.objects.create(user=instance)
