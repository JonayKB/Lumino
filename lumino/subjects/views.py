from django.shortcuts import render, redirect
from shared.decorators import student_required, teacher_required
from .models import Lesson, Subject,Enrollment
from django.contrib.auth.decorators import login_required
from .forms import SubjectEnrollForm, SubjectUnenrollForm,  EnrollmentMarkFormSet
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
    return render(request, 'subjects/enrollment/enroll.html', {'form': form})


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
    return render(request, 'subjects/enrollment/unenroll.html', {'form': form})

@login_required
@teacher_required
def mark_list(request, subject: Subject):
    if subject.teacher != request.user: return
    return render(request,'subjects/enrollment/mark_list.html',{'subject':subject})


## TODO
@login_required
@teacher_required
def edit_marks(request, subject: Subject ):
    if subject.teacher != request.user: return

    if request.method == 'POST':
        formset = EnrollmentMarkFormSet(request.POST, queryset=subject.enrollments.all())
        if (formset := EnrollmentMarkFormSet(request.POST, queryset=subject.enrollments.all())).is_valid():
            formset.save()
            messages.success(request,"Marks were successfully saved.")
            return redirect('subjects:mark-list', subject=subject)
        
    else:
        formset = EnrollmentMarkFormSet(queryset=subject.enrollments.all())

    return render(request,'subjects/enrollment/edit_marks.html',{'formset':formset,'subject':subject})


@login_required
@student_required
def request_certificate(request):
    pass