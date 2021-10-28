from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=100)
    about = models.TextField()

    