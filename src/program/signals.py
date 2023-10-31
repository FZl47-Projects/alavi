from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DietProgram

from notification.models import NotificationUser


# DietProgram post_save signal
@receiver(post_save, sender=DietProgram)
def send_user_notification(sender, instance, created, *args, **kwargs):
    if created:
        user = instance.user

        # Create notify for user
        NotificationUser.objects.create(
            type='DIET_PROGRAM_ADD',
            to_user=user,
            title='برنامه غذایی جدید برای شما ثبت شده است',
            description="""
                            برنامه غذایی جدید برای شما ثبت شده است
                        """,
            send_notify=True
        )
