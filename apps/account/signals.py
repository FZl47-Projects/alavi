from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, User


# User model save receiver(Profile)
@receiver(post_save, sender=User)
def user_model_saved(sender, instance, created, *args, **kwargs):
    if created:
        # Create profile for new user
        UserProfile.objects.create(user=instance)
