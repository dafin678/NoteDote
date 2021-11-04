from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) # Delete profile when user is deleted
    name = models.CharField(max_length=100)
    about = models.TextField(default="About Me")
    image_name = models.CharField(max_length=6, default = '1.jpg')
    
    def save(self, *args, **kwargs):
        super().save()
        if self.pk is None:
            self.name = self.user.username