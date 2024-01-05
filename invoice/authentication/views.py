from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LoginView

# Create your views here.
def authlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
 
        else:
            print('inavlid username or password')

    return render(request, 'authentication/login.html')



def authlogout(request):
    logout(request)
    return redirect('login')


def registration(request):
    return render(request, 'authentication/registration.html')


def forgetpassword(request):
    return render(request, 'authentication/forget.html')
