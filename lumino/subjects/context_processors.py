from .models import Subject

def get_user_subjects(request):
    if request.user.is_authenticated:
        subjects = Subject.objects.filter(students=request.user)
        return {'user_subjects': subjects}

    return {}