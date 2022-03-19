from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CunstomUserCreationForm


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact='')
    otherSkills = profile.skill_set.filter(description='')
    context = {'profile': profile, 'topSkills': topSkills,
               'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)


def loginUser(request):
    page = 'login'
    context = {'page': page}
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            pass
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'User name or password is not correct')
    return render(request, 'users/login-register.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'User logout')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CunstomUserCreationForm()

    if request.method == 'POST':
        form = CunstomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Account was created')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error has occured during register')

    context = {'page': page, 'form': form}
    return render(request, 'users/login-register.html', context)
