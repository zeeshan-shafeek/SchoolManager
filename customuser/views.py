from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, 'dashboard.html')




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