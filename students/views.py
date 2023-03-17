from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def studentHome(request):
    return render(request, 'student_home.html')