from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= "home"),

    path('course/<str:pk>/', views.course, name= "course"),
    path('courses/', views.courses, name= "courses"),
    path('create_course/', views.createCourse, name= "create_course"),
    path('update_course/<str:pk>/', views.updateCourse, name= "update_course"),
    path('delete_course/<str:pk>/', views.deleteCourse, name= "delete_course"),

    path('task/<str:pk>/', views.task, name= "task"),
    path('create_task/', views.createTask, name= "create_task"),
    path('create_task/<str:pk>', views.createTask, name= "create_task"),
    
    path('update_task/<str:pk>/', views.updateTask, name= "update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name= "delete_task"),
    path('close_task/<str:pk>/', views.closeTask, name= "close_task"),



    path('delete_course/<str:pk>/', views.deleteCourse, name= "delete_course"),

    path('students/', views.students, name= "students"),
    

]