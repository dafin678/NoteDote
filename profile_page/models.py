from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) # Delete profile when user is deleted
    name = models.CharField(max_length=100, blank=False)
    about = models.TextField(default="Hello!")
    image_name = models.CharField(max_length=20, default = 'default.jpg', blank=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.name = self.user.username
        super().save()