from django.shortcuts import render, redirect
from subjects.decorators import student_required, teacher_required
from .models import Lesson, Subject
from django.contrib.auth.decorators import login_required
from .forms import SubjectEnrollForm, SubjectUnenrollForm
from django.contrib import messages

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
def enroll_subjects(request):
    if request.method == 'POST':
        if (form := SubjectEnrollForm(request.user.pk, request.POST)).is_valid():
            form.save(request.user)
            messages.success(request, "Successfully enrolled in the chosen subjects.")
            return redirect('subjects:subject-list')
    else:
        form = SubjectEnrollForm(request.user.pk)
    return render(request, 'subjects/subject/enroll.html', {'form': form})


@login_required
@student_required
def unenroll_subjects(request):
    if request.method == 'POST':
        if (form := SubjectUnenrollForm(request.user.pk, request.POST)).is_valid():
            form.save(request.user)
            messages.success(request, "Successfully unenrolled from the chosen subjects.")
            return redirect('subjects:subject-list')
    else:
        form = SubjectUnenrollForm(request.user.pk)
    return render(request, 'subjects/subject/unenroll.html', {'form': form})

@login_required
@teacher_required
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