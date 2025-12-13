def get_user_subjects(request):
    user = request.user
    if user.is_authenticated:
        if user.profile.is_teacher():
            subjects = user.teaching.all()
        if user.profile.is_student():
            subjects = user.enrolled.all()
        return {'user_subjects': subjects}

    return {}