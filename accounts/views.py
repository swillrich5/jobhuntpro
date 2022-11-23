from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError



def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'accounts/signupaccount.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.ojbects.create_user(request.POST['username'],
                    password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('jobhunt:job_detail')
            except IntegrityError:
                return render(request, 'accounts/signupaccount.html', {
                    'form': UserCreateForm,
                    'error': 'Username already taken. Please choose another.'
                })
        else:
            return render(request, 'accounts/signupaccount.html',
                            {'form': UserCreateForm,
                             'error': 'Passwords do not match'})


def logoutaccount(request):
    logout(request)
    return redirect('jobhunt:job_list')



def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'accounts/loginaccount.html', {
                        'form': AuthenticationForm
                     })
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/loginaccount.html',
                            { 'form': AuthenticationForm(),
                              'error': 'Username and Password do not match'})
        else:
            login(request, user)
            return redirect('jobhunt:job_list')    