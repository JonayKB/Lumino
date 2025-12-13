from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect



def teacher_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.profile.is_teacher():
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper

def student_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.profile.is_student():
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper