from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', views.home, name= "home"),
    path('login/', views.loginpage, name= "login"),
    path('logout/', views.logoutUser, name= "logout"),
    path('register/', views.register, name= "register"),
    path('students/', views.students, name= "students")

]