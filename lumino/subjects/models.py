from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='enrollments',
        on_delete=models.CASCADE,
    )
    subject = models.ForeignKey(
        'subjects.Subject',
        related_name='enrollments',
        on_delete=models.CASCADE,
    )
    enrolled_at = models.DateField(auto_now_add=True)
    mark = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True
    )

    def __str__(self):
        return f'{self.student} enrolled in {self.subject}'


class Subject(models.Model):
    code = models.CharField(unique=True)
    name = models.CharField(max_length=128)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='teaching', on_delete=models.PROTECT
    )

    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='enrolled',
        through=Enrollment,
        blank=True,
    )

    def __str__(self):
        return f'{self.code} - {self.name}'

    def get_absolute_url(self):
        return reverse('subjects:subject-detail', args=[self])

    def enroll(self, student):
        Enrollment.objects.create(student=student, subject=self)

    def unenroll(self, student):
        Enrollment.objects.filter(student=student, subject=self).delete()


class Lesson(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='lessons',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return f'Lesson: {self.title} of {self.subject}'

    def get_absolute_url(self):
        return reverse('subjects:lesson-detail', args=[self.subject, self])
