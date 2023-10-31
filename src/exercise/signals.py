from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ExerciseProgram

from notification.models import NotificationUser


# ExerciseProgram post_save signal
@receiver(post_save, sender=ExerciseProgram)
def send_user_notification(sender, instance, created, **kwargs):
    if created:
        user = instance.user

        # Create notify for user
        NotificationUser.objects.create(
            type='TRAINING_PROGRAM_ADD',
            to_user=user,
            title='برنامه تمرینی جدید برای شما ثبت شده است',
            description="""
                            برنامه تمرینی جدید برای شما ثبت شده است
                        """,
            send_notify=True
        )
