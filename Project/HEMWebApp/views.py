from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Project


# Create your views here.

def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('userindex')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')

    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')

        # Check if passwords match
        if password != confirm_password:
            # Handle password mismatch error
            messages.error(request, 'Password do not match!')
            return redirect('signup')

        # Create user
        User.objects.create_user(
            email=email,
            password=password,
            username=username,
        )
        return redirect('login')

    return render(request, 'signup.html')


@login_required
def userindex_views(request):
    first_name = request.user.first_name
    last_name = request.user.last_name

    data = {
        'user': request.user,
        'name': first_name + ' ' + last_name,
    }

    return render(request, 'index.html', data)


@login_required
def homepage_view(request):
    return render(request, 'homepage.html')


@login_required
def logout_action(request):
    logout(request)
    return redirect('index')


@login_required
def room_view(request):
    user = request.user

    data = {
        'user': user,
    }
    return render(request, 'mainpage.html', data)


@login_required
def createproject_view(request):
    if request.method == 'POST':
        projectname = request.POST.get('projectname')
        numroom = request.POST.get('numroom')
        Project.objects.create(
            name=projectname,
            numroom=numroom,
            created_by=request.user,
        )
        return redirect('rooms')

    user = request.user

    data = {
        'user': user,
    }

    return render(request, 'newproject.html', data)
