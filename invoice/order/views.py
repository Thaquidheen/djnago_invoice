from django.shortcuts import render
from customer.models import AddCustomer 
  # Create your views here.

def orders(request):
    customers = AddCustomer.objects.all()
    
    diction ={'custid':customers }
    return render(request,'order.html',context=diction)