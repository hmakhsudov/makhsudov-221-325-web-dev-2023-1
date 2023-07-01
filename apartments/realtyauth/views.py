from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)  # Log in the user
            messages.success(request, 'Успешная регистрация!')
            return redirect('index')  # Replace 'home' with the desired URL after registration
    else:
        form = CustomUserCreationForm()
    return render(request, './register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # User is authenticated, log in the user
            login(request, user)
            messages.success(request, 'Успешная Авторизация!')
            return redirect('index')  # Replace 'home' with the URL name of your home page
        else:
            # Invalid credentials, display an error message
            error_message = 'Неправильно введен логин или пароль'
            return render(request, './login.html', {'error_message': error_message})
    
    return render(request, './login.html')

def logout_view(request):
    logout(request)
    return redirect('index')  # Replace 'home' with the desired URL after logout