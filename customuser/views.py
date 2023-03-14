from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from School.models import *
# Create your views here.

def home(request):
    courses = Course.objects.all()
    tasks = Task.objects.all()
    tasks_count = tasks.count()
    active_count = tasks.filter(status= Task.ACTIVE).count()
    closed_count = tasks.filter(status= Task.CLOSED).count()


    context = {
        'courses': courses,
        'tasks': tasks,
        'tasks_count': tasks_count,
        'active_count': active_count,
        'closed_count': closed_count

    }


    return render(request, 'dashboard.html', context)

def students(request):
    students = Student.objects.all()

    return render(request, 'students.html', {'students' : students})



def logoutUser(request):
    logout(request)
    return redirect("login")



def loginpage(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect!')
    context = {}
    return render(request, 'login.html', context)


def register(request):
    form = CustomUserCreationForm()


    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form.errors.as_text)
        if form.is_valid and not form.errors:
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request, f'Account was created for {user}')
            return redirect('login')



    context = {'form' : form}
    return render(request, 'register.html', context) 