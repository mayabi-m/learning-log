from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('learning_logs:index')  # Redirect to a success page.
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')
# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('learning_logs:index')  # Redirect to a success page.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('learning_logs:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})    