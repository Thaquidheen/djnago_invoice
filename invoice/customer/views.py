from django.shortcuts import render
from .models import AddCustomer
from django.contrib import messages
# Create your views here.
def addcustomer(request):
    if request.method == 'POST':
        customer_name=request.POST.get('customer_name')
        addCustomerdata= AddCustomer(customer_name=customer_name)
        addCustomerdata.save()
        messages.success(request,'Item added successfully')
    return render(request,'customer.html')