from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from users.models import Profile


def role_required(request, role, func, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.profile.role == role:
        raise PermissionDenied
    return func(request, *args, **kwargs)


def teacher_required(func):
    def wrapper(request, *args, **kwargs):
        return role_required(request, Profile.Role.TEACHER, func, *args, **kwargs)

    return wrapper


def student_required(func):
    def wrapper(request, *args, **kwargs):
        return role_required(request, Profile.Role.STUDENT, func, *args, **kwargs)

    return wrapper


def user_is_subject_teacher(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.profile.is_teacher() or kwargs['subject'].teacher != request.user:
            raise PermissionDenied
        return func(request, *args, **kwargs)

    return wrapper
