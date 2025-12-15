from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Profile
from django.contrib.auth import get_user_model


@receiver(post_save, sender=get_user_model())
def create_profile_signal(sender, instance, created, raw, using, update_fields, **kwargs):
    if created and not raw:
        Profile.objects.create(user=instance)


