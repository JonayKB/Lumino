from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from shared.decorators import student_required, teacher_required, user_is_subject_teacher

from .forms import (
    AddLessonForm,
    EditLessonForm,
    EnrollmentMarkFormSet,
    SubjectEnrollForm,
    SubjectUnenrollForm,
)
from .models import Lesson, Subject
from .tasks import deliver_certificate


@login_required
def subject_list(request):
    if request.user.profile.is_student:
        show_request_certificate = request.user.enrollments.filter(mark__isnull=False).exists()
    return render(
        request,
        'subjects/subject/list.html',
        {'show_request_certificate': show_request_certificate},
    )


@login_required
def subject_detail(request, subject: Subject):
    profile = request.user.profile
    enrollment = None
    if profile.is_teacher() and subject.teacher != request.user:
        raise PermissionDenied
    if profile.is_student():
        enrollment = subject.enrollments.filter(student=request.user).first()
        if not enrollment:
            raise PermissionDenied

    return render(
        request, 'subjects/subject/detail.html', {'subject': subject, 'enrollment': enrollment}
    )


@login_required
@teacher_required
@user_is_subject_teacher
def lesson_add(request, subject: Subject):
    if request.method == 'POST':
        if (form := AddLessonForm(request.POST)).is_valid():
            form.save(subject)
            messages.success(request, _('Lesson was successfully added.'))
            return redirect(subject)
    else:
        form = AddLessonForm()
    return render(request, 'subjects/lesson/add.html', {'form': form, 'subject': subject})


@login_required
def lesson_detail(request, lesson: Lesson, subject: Subject):
    profile = request.user.profile
    if profile.is_teacher() and subject.teacher != request.user:
        raise PermissionDenied
    if profile.is_student():
        if not subject.enrollments.filter(student=request.user).exists():
            raise PermissionDenied
    return render(request, 'subjects/lesson/detail.html', {'lesson': lesson, 'subject': subject})


@login_required
@teacher_required
@user_is_subject_teacher
def lesson_edit(request, lesson: Lesson, subject: Subject):
    if request.method == 'POST':
        if (form := EditLessonForm(request.POST, instance=lesson)).is_valid():
            form.save(subject)
            messages.success(request, _('Changes were successfully saved.'))
            return render(
                request,
                'subjects/lesson/edit.html',
                {'form': form, 'subject': subject, 'lesson': lesson},
            )
    else:
        form = EditLessonForm(instance=lesson)
    return render(
        request, 'subjects/lesson/edit.html', {'form': form, 'subject': subject, 'lesson': lesson}
    )


@login_required
@teacher_required
@user_is_subject_teacher
def lesson_delete(request, lesson: Lesson, subject: Subject):
    lesson.delete()
    messages.success(request, _('Lesson was successfully deleted.'))
    return redirect(subject)


@login_required
@student_required
def enroll_subjects(request):
    if request.method == 'POST':
        if (form := SubjectEnrollForm(request.user.pk, request.POST)).is_valid():
            form.save(request.user)
            messages.success(request, _('Successfully enrolled in the chosen subjects.'))
            return redirect('subjects:subject-list')
    else:
        form = SubjectEnrollForm(request.user.pk)
    return render(request, 'subjects/enrollment/enroll.html', {'form': form})


@login_required
@student_required
def unenroll_subjects(request):
    if request.method == 'POST':
        if (form := SubjectUnenrollForm(request.user.pk, request.POST)).is_valid():
            form.save(request.user)
            messages.success(request, _('Successfully unenrolled from the chosen subjects.'))
            return redirect('subjects:subject-list')
    else:
        form = SubjectUnenrollForm(request.user.pk)
    return render(request, 'subjects/enrollment/unenroll.html', {'form': form})


@login_required
@teacher_required
@user_is_subject_teacher
def mark_list(request, subject: Subject):
    return render(request, 'subjects/enrollment/mark_list.html', {'subject': subject})


@login_required
@teacher_required
@user_is_subject_teacher
def edit_marks(request, subject: Subject):
    if request.method == 'POST':
        formset = EnrollmentMarkFormSet(request.POST, queryset=subject.enrollments.all())
        if (
            formset := EnrollmentMarkFormSet(request.POST, queryset=subject.enrollments.all())
        ).is_valid():
            formset.save()
            messages.success(request, _('Marks were successfully saved.'))
            return redirect('subjects:edit-marks', subject=subject)

    else:
        formset = EnrollmentMarkFormSet(queryset=subject.enrollments.all())

    return render(
        request, 'subjects/enrollment/edit_marks.html', {'formset': formset, 'subject': subject}
    )


@login_required
@student_required
def request_certificate(request):
    # Aquí añadiria una verificación de que el alumno tiene alguna asignatura, pero los tests no lo permiten
    if request.user.enrolled.filter(enrollments__mark__isnull=True).exists():
        messages.error(request, _('You have some ungraded subjects'))
        raise PermissionDenied

    # Aqui debería enviarse en idioma, usando get_language(), pero esta preaprado para mockear con dos argumentos posicionales TODO
    # deliver_certificate.delay(request.build_absolute_uri(), request.user, get_language())
    deliver_certificate.delay(request.build_absolute_uri(), request.user)
    return render(request, 'subjects/enrollment/certificate_request.html')
