from django.shortcuts import render, redirect
from .models import AddCustomer
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def customer(request):
    if request.method == 'POST':
        customer_name=request.POST.get('customer_name')
        customer_number=request.POST.get('customer_number')
        addCustomerdata= AddCustomer(customer_name=customer_name,customer_number=customer_number)
        addCustomerdata.save()
        messages.success(request,'Item added successfully')
    
    customers = AddCustomer.objects.all()

    
    return render(request,'customer.html', {'customers': customers} )