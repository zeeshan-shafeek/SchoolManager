from django.shortcuts import render
from .form import CustomUserCreationForm

# Create your views here.


def login(request):
    return render(request, 'login.html')


def register(request):
    form = CustomUserCreationForm()


    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
        



    context = {'form' : form}
    return render(request, 'register.html', context) 