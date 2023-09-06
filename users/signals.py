from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Signal receiver function that creates a Profile when a User instance is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Create a new Profile for the newly created User instance
        Profile.objects.create(user=instance)

# Signal receiver function that saves the Profile when the related User instance is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    try:
        # Check if the User instance has a related Profile
        if Profile.objects.filter(user=instance).first():
            # Save the Profile instance related to the User
            instance.profile.save()
    except:
        # If there is any exception while saving the profile, simply pass
        pass
