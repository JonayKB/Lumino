from django.shortcuts import render
from .models import Subject

def subject_list(request):
    return render(request, 'subjects/subject/list.html')

def subject_detail(request, subject: Subject):
    pass
    
    
