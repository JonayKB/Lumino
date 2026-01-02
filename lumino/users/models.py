from django.db import models
from django.conf import settings
from django.urls import reverse

class Profile(models.Model):
    class Role(models.TextChoices):
        STUDENT = 'S', 'Student'
        TEACHER = 'T', 'Teacher'
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to ='avatars',
        default='avatars/noavatar.png',
        blank=True
    )
    bio = models.TextField(max_length=265, blank=True)
    role = models.CharField(
        max_length= 1,
        choices=Role,
        default=Role.STUDENT
    )
    def __str__(self):
        return f"Profile of {self.user.username}"
    def is_student(self):
        return self.role == self.Role.STUDENT
    def is_teacher(self):
        return self.role == self.Role.TEACHER
    def get_absolute_url(self):
        return reverse('users:profile-detail', args=[self.user.username])
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"