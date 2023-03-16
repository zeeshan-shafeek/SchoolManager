from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .form import TaskForm, CourseForm
from django.contrib import messages
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

# @login_required
def courses(request):
    user = request.user
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

def createCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'course_form.html', context)

def updateCourse(request, pk):


    task = Course.objects.get(id= pk)
    form = CourseForm(instance= task)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance= task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'course_form.html', context)

def deleteCourse(request, pk):

    course = Course.objects.get(id= pk)
    if request.method == 'POST':
        course.delete()
        return redirect('home')

    context = {'item': course}
    return render(request, 'delete.html', context)



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

def createTask(request, pk= None):
    
    
    if pk:
        course = Course.objects.get(id= pk)
        form = TaskForm(instance= Task(course= course))
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('course', pk= pk)

        context = {'form': form}
        return render(request, 'task_form.html', context)
    else:
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
            return redirect('task', pk= pk)

    context = {'form': form}
    return render(request, 'task_form.html', context)

def deleteTask(request, pk):

    task = Task.objects.get(id= pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'item': task}
    return render(request, 'delete.html', context)

def closeTask(request, pk):
    task = Task.objects.get(id= pk)
    task.status = Task.CLOSED
    task.save()
    return redirect('task', pk= pk)
    
