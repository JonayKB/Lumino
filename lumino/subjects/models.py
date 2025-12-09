from django.db import models
from django.conf import settings

from django.core.validators import MinValueValidator, MaxValueValidator


class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='enrollment',
        on_delete=models.CASCADE,
    )

    subject = models.ForeignKey(
        'subjects.Subject',
        related_name='enrollment',
        on_delete=models.CASCADE,
    )
    enrolled_at = models.DateField(auto_now_add=True),
    mark = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )

class Subject(models.Model):
    code = models.CharField(primary_key=True)
    name = models.CharField(max_length=128)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='subjects',
        on_delete=models.PROTECT
    )

    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='subjects',
        through= Enrollment,
        blank=True,
    ) 


