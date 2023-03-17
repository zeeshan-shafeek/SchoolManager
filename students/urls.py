from django.urls import path

from . import views


urlpatterns = [
    path('', views.studentHome, name= 'student_home'),
    

]