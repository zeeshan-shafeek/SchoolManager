from django.shortcuts import render, redirect
from .form import CustomUserCreationForm, TaskForm
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

def courses(request):
    courses = Course.objects.all()

    return render(request, 'courses.html', {'courses' : courses})


def course(request, pk):
    course = Course.objects.get(id= pk)
    tasks = course.task_set.all()
    student_count = course.students.all().count()

    context = {
        'course' : course,
        'student_count': student_count,
        'tasks': tasks,
    }
    return render(request, 'course.html', context)

def task(request, pk):
    task = Task.objects.get(id= pk)
    students_task = task.studenttask_set.all()
    student_count = students_task.count()

    context = {
            'task' : task,
            'students_task' : students_task,
            'student_count' : student_count,
            }
    
    return render(request, 'task.html', context)

def createTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'task_form.html', context)

def updateTask(request, pk):


    task = Task.objects.get(id= pk)
    form = TaskForm(instance= task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance= task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'task_form.html', context)





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