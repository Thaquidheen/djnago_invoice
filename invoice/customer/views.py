from django.shortcuts import render, redirect
from .models import addcustomer
from django.contrib import messages
# Create your views here.
def customer(request):
    if request.method == 'POST':
        customer_name=request.POST.get('customer_name')
        customer_number=request.POST.get('customer_number')
        addCustomerdata= addcustomer(customer_name=customer_name,customer_number=customer_number)
        addCustomerdata.save()
        messages.success(request,'Item added successfully')

    return render(request,'customer.html')