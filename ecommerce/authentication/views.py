
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method == 'POST':
        # Get the user information from the form
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        
        # Basic validation checks
        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return redirect('signup')
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('signup')
        
        # Create the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, "Your account has been created successfully.")
            return redirect('handlelogin')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('signup')
    
    return render(request, 'signup.html')


def handlelogin(request):
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('handlelogin')
    
    return render(request, 'login.html')


def handlelogout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('handlelogin')  # Redirect to login page
