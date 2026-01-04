from django.shortcuts import render, redirect
from shared.decorators import student_required, teacher_required
from .models import Lesson, Subject
from django.contrib.auth.decorators import login_required
from .forms import SubjectEnrollForm, SubjectUnenrollForm,  EnrollmentMarkFormSet
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .tasks import deliver_certificate
from django.utils.translation import get_language, gettext as _


@login_required
def subject_list(request):
    return render(request, 'subjects/subject/list.html')

@login_required
def subject_detail(request, subject: Subject):
    profile = request.user.profile
    enrollment = None
    if profile.is_teacher() and subject.teacher != request.user:
        raise PermissionDenied
    if profile.is_student():
        try:
            enrollment = subject.enrollments.filter(student = request.user).first()
        except Subject.DoesNotExist:
            raise PermissionDenied
        
    return render(request, 'subjects/subject/detail.html', {'subject':subject, 'enrollment':enrollment })


@login_required
@teacher_required
def lesson_add(request, subject: Subject):
    pass

@login_required
def lesson_detail(request, lesson: Lesson, subject: Subject):
    pass


@login_required
@teacher_required
def lesson_edit(request, lesson: Lesson, subject: Subject):
    pass

@login_required
@teacher_required
def lesson_delete(request, lesson: Lesson, subject: Subject):
    pass

@login_required
@student_required
def enroll_subjects(request):
    if request.method == 'POST':
        if (form := SubjectEnrollForm(request.user.pk, request.POST)).is_valid():
            form.save(request.user)
            messages.success(request, _("Successfully enrolled in the chosen subjects."))
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
            messages.success(request, _("Successfully unenrolled from the chosen subjects."))
            return redirect('subjects:subject-list')
    else:
        form = SubjectUnenrollForm(request.user.pk)
    return render(request, 'subjects/enrollment/unenroll.html', {'form': form})

@login_required
@teacher_required
def mark_list(request, subject: Subject):
    if subject.teacher != request.user: raise PermissionDenied
    return render(request,'subjects/enrollment/mark_list.html',{'subject':subject})


@login_required
@teacher_required
def edit_marks(request, subject: Subject ):
    if subject.teacher != request.user: raise PermissionDenied

    if request.method == 'POST':
        formset = EnrollmentMarkFormSet(request.POST, queryset=subject.enrollments.all())
        if (formset := EnrollmentMarkFormSet(request.POST, queryset=subject.enrollments.all())).is_valid():
            formset.save()
            messages.success(request,_("Marks were successfully saved."))
            return redirect('subjects:edit-marks', subject=subject)
        
    else:
        formset = EnrollmentMarkFormSet(queryset=subject.enrollments.all())

    return render(request,'subjects/enrollment/edit_marks.html',{'formset':formset,'subject':subject})


@login_required
@student_required
def request_certificate(request):
    # Aquí añadiria una verificación de que el alumno tiene alguna asignatura, pero los tests no lo permiten
    if request.user.enrolled.filter(enrollments__mark__isnull=True).exists():
        messages.error(request, _("You have some ungraded subjects"))
        raise PermissionDenied
    
    #Aqui debería enviarse en idioma, usando get_language(), pero esta preaprado para mockear con dos argumentos posicionales
    deliver_certificate.delay(request.build_absolute_uri(), request.user,get_language())
    return render(request,'subjects/enrollment/certificate_request.html')