from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from . import forms


def index(request):
    return render(request, 'core/index.html')


@login_required
def special(request):
    return HttpResponse('You are logged in.')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponse(request, 'core/index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reversed('index'))
            else:
                return HttpResponse("Account blocked.")
        else:
            print('Logging tentative failed.')
            print('Username: {} and password {}'.format(username, password))
            return HttpResponse('Invalid login inputs.')
    else:
        return render(request, 'core/login.html', {})


def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'core/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})
