from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView

User = get_user_model()

# Create your views here.
def home(request):
    return render(request,'accounts/home.html')

# def user(request):
#     return render(request, 'accounts/user.html')

# def admin(request):
#     return render(request, 'accounts/admin.html')

def admin(request):
    if request.user.role == 'admin':
        return render(request, 'accounts/admin.html')
    else:
        return redirect('home')
    
def user(request):
    if request.user.role == 'user':
        return render(request, 'accounts/user.html')
    else:
        return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.role == 'admin':
                login(request, user)
                return render(request, 'accounts/admin.html', {'alert_message': 'Logged in successfully as admin!'})
            elif user.role == 'user':
                login(request, user)
                return render(request, 'accounts/user.html', {'alert_message': 'Logged in successfully as user!'})
        else:
            return render(request, 'accounts/login.html', {'alert_message': 'Invalid username or password'})
            
    return render(request, 'accounts/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        role = request.POST.get('role','user')
        
        if User.objects.filter(username = username).exists():
            messages.error(request, 'Username already exists')
            
        else:
            user = User.objects.create_user(username=username,password=password,email=email,role=role)
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def password_reset_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        new_password = request.POST['new_password']
        
        user = User.objects.get(username=username)
        
        if user:
            user.set_password(new_password)
            user.save()
            login(request, user)
            return redirect('home')
            
        else:
            messages.error(request, 'Username not exists')
     
    return render(request, 'accounts/password_reset.html')   