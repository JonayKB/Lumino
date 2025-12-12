from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Profile

@login_required
def user_detail(request, profile: Profile):
    pass

@login_required
def user_edit(request):
    pass

@login_required
def user_leave(request):
    pass