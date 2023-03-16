from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    
    path('login/', views.loginpage, name= "login"),
    path('logout/', views.logoutUser, name= "logout"),
    path('register/', views.register, name= "register"),
    
]