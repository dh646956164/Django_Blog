from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
# from django.core.files import FILE  # This line is not used, so it's commented out
import PIL
from PIL import Image

# Creating a Profile model to extend the built-in Django User model
class Profile(models.Model):
    # Creating a one-to-one relationship between the User and Profile models
    # The related_name 'profile' allows us to access the profile from the user instance using user.profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Adding an image field to store the user's profile image
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # Defining the string representation of the Profile model
    def __str__(self):
        return f'{self.user.username} Profile'
