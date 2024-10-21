
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        # Get the user information from the form
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        # Basic validation checks
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        # Check if the user already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists.")
            return redirect('signup')
        
        # Create the user
        try:
            user = User.objects.create_user(username=email, email=email, password=password1)
            user.save()
            messages.success(request, "User created successfully.")
            return redirect("handlelogin")  # Redirect to 'handlelogin'
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('signup')

    return render(request, 'signup.html')

def handlelogin(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user exists and authenticate
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('index')  # or another appropriate redirect
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('handlelogin')  # Redirect back to login page with message

    return render(request, 'login.html')


def handlelogout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('handlelogin')  # Redirect to login page
