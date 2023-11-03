from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def contact(request):
    return render(request, 'home/contact.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            # Return an 'invalid login' error message.
            pass
    return render(request, 'home/login.html')

def logout_view(request):
    logout(request)
    return redirect('home:index')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'home/register.html', {'form': form})
