from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect



def teacher_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.profile.is_teacher():
            raise PermissionDenied
        return func(request, *args, **kwargs)
    return wrapper

def student_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.profile.is_student():
            raise PermissionDenied
        return func(request, *args, **kwargs)
    return wrapper

def user_is_subject_teacher(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.profile.is_teacher() or kwargs['subject'].teacher != request.user:
            raise PermissionDenied
        return func(request, *args, **kwargs)
    return wrapper