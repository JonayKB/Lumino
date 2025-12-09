from django.db import models
from django.conf import settings

class Profile(models.Model):
    class Role(models.TextChoices):
        TEACHER = 'T', 'Teacher'
        STUDENT = 'S', 'Student'
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to ='avatars',
        default='avatars/noavatar.png'
    )
    bio = models.CharField(max_length=265, blank=True)
    role = models.CharField(
        max_length= 1,
        choices=Role,
        default=Role.STUDENT
    )