from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', views.home, name= "home"),
    path('login/', views.loginpage, name= "login"),
    path('logout/', views.logoutUser, name= "logout"),
    path('register/', views.register, name= "register"),
    path('course/<str:pk>/', views.course, name= "course"),
    path('courses/', views.courses, name= "courses"),
    path('students/', views.students, name= "students"),
    path('task/<str:pk>/', views.task, name= "task"),
    path('create_task', views.createTask, name= "create_task"),
    path('update_task/<str:pk>/', views.updateTask, name= "update_task"),

]