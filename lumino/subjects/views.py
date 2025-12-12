from django.shortcuts import render
from subjects.decorators import student_required, teacher_required
from .models import Lesson, Subject
from django.contrib.auth.decorators import login_required

@login_required
def subject_list(request):
    return render(request, 'subjects/subject/list.html')

@login_required
def subject_detail(request, subject: Subject):
    pass

@login_required
@teacher_required
def lesson_add(request, lesson: Lesson):
    pass

@login_required
def lesson_detail(request, lesson: Lesson):
    pass


@login_required
@teacher_required
def lesson_edit(request, lesson: Lesson):
    pass

@login_required
@teacher_required
def lesson_delete(request, lesson: Lesson):
    pass

@login_required
@student_required
def enroll_subject(request, subject: Subject):
    pass

@login_required
@student_required
def unenroll_subject(request, subject: Subject):
    pass

@login_required
@student_required
def mark_list(request, subject: Subject):
    pass

@login_required
@teacher_required
def edit_marks(request, subject: Subject ):
    pass

@login_required
@student_required
def request_certificate(request):
    pass