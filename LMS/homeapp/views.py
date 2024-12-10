from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from .models import User_types


def userSplitterView(request):
    user_id = request.user.id
    user_type = User_types.objects.get(user_id=user_id)
    if user_type.user_type ==  'INS':
        return redirect('instructor_dashboard')
    elif user_type.user_type ==  'STU':
        return redirect('student_dashboard')
    elif user_type.user_type ==  'ADM':
        return redirect('home')
    else:
        return HttpResponse("Error user_type={user_type}, user_type.user_type={user_type.user_type}")

@login_required(login_url="/login/")
def logoutView(request):
    logout(request)
    return redirect('login')

def loginView(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return redirect('userSplitterView')
                return redirect('/redirect/')
            else:
                messages.add_message(request, messages.ERROR, "Invalid username or password")
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('userSplitterView')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required(login_url="/login/")
def home(request):
    user_type = User_types.objects.get(user_id=request.user.id)

    # Check if the user is a student (user_type = 'STU')
    if user_type.user_type:
        user_info = {
            'username': request.user.username,
            'email': request.user.email,
        }
        return render(request, 'home.html', {'user_info': user_info})
    else:
        return redirect('userSplitterView')