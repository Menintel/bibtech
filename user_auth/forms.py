from django.shortcuts import render, redirect
from .forms import ReaderRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = ReaderRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_reader = True
            user.save()
            return redirect('login')
    else:
        form = ReaderRegistrationForm()
    return render(request, 'user_auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_lib_staff:
                return redirect('staff_dashboard')
            elif user.is_reader:
                return redirect('reader_dashboard')
            else:
                messages.error(request, "User has no assigned role.")
    else:
        form = AuthenticationForm()
    return render(request, 'user_auth/login.html', {'form': form})