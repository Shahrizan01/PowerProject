from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


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
            return redirect('homepage')
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

def homepage_view(request):
    if request.user.is_authenticated == True:
        return render(request, 'homepage.html')
    else:
        return redirect('login')


def logout_view(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    
    if username != None:
        logout(request)
        return redirect(index)
