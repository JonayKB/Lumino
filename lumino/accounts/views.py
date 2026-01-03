from django.shortcuts import render, redirect
from .forms import LoginForm,SignupForm
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.utils.translation import gettext as _


FALLBACK_URL = 'index'

def user_login(request):

    if(request.user.is_authenticated):
        return redirect(FALLBACK_URL)
    if request.method == 'POST':
        if (form := LoginForm(request.POST)).is_valid():
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           if user := authenticate(request,username=username, password=password):
               login(request,user)
               return redirect(request.GET.get('next', FALLBACK_URL))
           else:
                form.add_error(None, _("Incorrect username or password"))
    else:
        form = LoginForm()
    return render(request,'accounts/login.html', {'form':form, 'hide_links': True})

def user_logout(request):
    logout(request)
    return redirect(reverse(FALLBACK_URL))

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(FALLBACK_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html',{'form':form, 'hide_links': True})

