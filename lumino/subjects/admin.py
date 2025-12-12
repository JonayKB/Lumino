from django.contrib import admin
from .models import Subject, Lesson, Enrollment

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass

@admin.register(Enrollment)
class EnrrollmentAdmin(admin.ModelAdmin):
    pass
