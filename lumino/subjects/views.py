from django.shortcuts import render
from users.models import Profile

def subject_list(request):
    subjects = request.user.subjects.all()

    return render(request, 'subjects/subject/list.html', {'subjects': subjects })
    
    
