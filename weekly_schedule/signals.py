# from django.db.models.signals import post_save #Import a post_save signal when a user is created
# from django.contrib.auth.models import User # Import the built-in User model, which is a sender
# from django.dispatch import receiver

# from weekly_schedule.models import Weekly_schedule # Import the receiver

# @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
# def save_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         profile = UserProfile(user=user)
#         profile.save()
#         Weekly_schedule.objects.create(user=instance)

from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from .models import Weekly_schedule

@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Weekly_schedule.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()