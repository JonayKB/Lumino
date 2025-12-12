from django.contrib import admin
from .models import Subject, Lesson, Enrollment

class SubjectEnrollmentDetailInLine(admin.TabularInline):
    model = Enrollment
    extra = 1

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    inlines = [SubjectEnrollmentDetailInLine]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass

@admin.register(Enrollment)
class EnrrollmentAdmin(admin.ModelAdmin):
    pass
