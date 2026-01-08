from django.shortcuts import get_object_or_404

from .models import Lesson, Subject


class SubjectConverter:
    regex = '[a-zA-Z]{3}'

    def to_python(self, subject_code):
        return get_object_or_404(Subject, code=subject_code)

    def to_url(self, subject: Subject):
        return subject.code


class LessonConverter:
    regex = '[0-9]+'

    def to_python(self, lesson_pk):
        return get_object_or_404(Lesson, pk=lesson_pk)

    def to_url(self, lesson: Lesson):
        return lesson.pk
