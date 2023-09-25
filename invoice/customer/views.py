from django.shortcuts import render, redirect
from .models import AddCustomer
from django.contrib import messages
# Create your views here.
def addcustomer(request):
    if request.method == 'POST':
        customer_name=request.POST.get('customer_name')
        addCustomerdata= AddCustomer(customer_name=customer_name)
        addCustomerdata.save()
        customer_id = addCustomerdata.id
        request.session['customer_id'] = customer_id
        messages.success(request,'Item added successfully')
        return redirect('order')
    return render(request,'customer.html')