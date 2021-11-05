from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) # Delete profile when user is deleted
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=100)
    about = models.TextField(default="About Me")
    
    
    def save(self, *args, **kwargs):
        super().save()

        if self.pk is None: # Set default name to username
            self.name = self.user.username
        
        img = Image.open(self.image.path)
        # Resize image to 250x250
        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)