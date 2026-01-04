from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from shared.decorators import student_required

from .forms import EditProfileForm
from .models import Profile


@login_required
def user_detail(request, profile: Profile):
    return render(request, 'users/profile/detail.html', {'profile': profile})


@login_required
def user_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        if (form := EditProfileForm(request.POST,request.FILES, instance=profile)).is_valid():
            profile =form.save()
            messages.success(request,_('User profile has been successfully saved.'))
            return redirect('users:profile-detail', profile.user.username)
    form = EditProfileForm(instance=profile)
    return render(request, 'users/profile/edit.html', {'form': form})


@login_required
@student_required
def user_leave(request):
    request.user.delete()
    logout(request)
    messages.success(request, _('Good bye! Hope to see you soon.'))
    return redirect('index')
