from django.shortcuts import render

# Create your views here.
def authlogin(request):
    return render(request, 'authentication/login.html')