from django.shortcuts import render,redirect

from .models import Item
from customer.models import AddCustomer




def additem(request):
    if request.method == 'POST':
 
        customer_name = request.POST.get('customer')
        item_name = request.POST.get('item_name')
        thickness = request.POST.get('thickness')
        size = request.POST.get('size')
        rate = request.POST.get('rate')


        customer, created = AddCustomer.objects.get_or_create(customer_name=customer_name)
        item = Item(customer=customer, item_name=item_name, thickness=thickness, size=size, rate=rate)
        item.save()
    
    customers = AddCustomer.objects.all()
        
    return render(request,'additem.html',{'customers': customers})