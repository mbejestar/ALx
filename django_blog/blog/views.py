from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate, logout  
from django.contrib.auth.decorators import login_required  
from .forms import UserRegistrationForm  
from django.contrib import messages  

# Registration View  
def register(request):  
    if request.method == 'POST':  
        form = UserRegistrationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            username = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password1')  
            user = authenticate(username=username, password=password)  
            login(request, user)  
            messages.success(request, 'Registration successful.')  
            return redirect('profile')  
    else:  
        form = UserRegistrationForm()  
    return render(request, 'blog/register.html', {'form': form})  

# Login View  
def login_view(request):  
    if request.method == 'POST':  
        username = request.POST['username']  
        password = request.POST['password']  
        user = authenticate(request, username=username, password=password)  
        if user is not None:  
            login(request, user)  
            return redirect('profile')  
        else:  
            messages.error(request, 'Invalid username or password.')  
    return render(request, 'blog/login.html')  

# Logout View  
def logout_view(request):  
    logout(request)  
    messages.info(request, 'Logged out successfully.')  
    return redirect('login')  

# Profile View  
@login_required  
def profile(request):  
    return render(request, 'blog/profile.html', {'user': request.user})  
