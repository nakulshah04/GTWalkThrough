from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created. Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Auth/register.html', {'form': form})

def login_view(request):
    from django.contrib.auth.forms import AuthenticationForm
    from django.contrib.auth import authenticate, login
    from django.shortcuts import render, redirect

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'Auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
