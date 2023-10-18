from django.shortcuts import render,redirect

from .models import *
from customer.models import AddCustomer




# def additem(request):
#     if request.method == 'POST':
#         customer_name = request.POST.get('customer_name')
#         item_name = request.POST.get('item_name')
#         size_value = request.POST.get('size_value')
#         rate_value = request.POST.get('rate_value')
#         thickness_value = request.POST.get('thickness_value')


#         customer, created = AddCustomer.objects.get_or_create(customer_name=customer_name)


#         item = Item(customer_name=customer, item_name=item_name)
#         item.save()


#         size = Size(item=item, size_value=size_value)
#         size.save()


#         rate = Rate(item=item, rate_value=rate_value)
#         rate.save()

   
#         thickness = Thickness(item=item, thickness_value=thickness_value)
#         thickness.save()
    
        
#     return render(request,'additem.html')
def additem(request):
    if request.method == 'POST':
        customer_name = request.POST['customer']
        item_name = request.POST['item_name']
        thickness = request.POST['thickness']
        size = request.POST['size']
        rate = request.POST['rate']
        
    
        customer, created = AddCustomer.objects.get_or_create(customer_name=customer_name)
        item, created = Item.objects.get_or_create(item_name=item_name, customer_name=customer)

        item_variation = ItemVariation.objects.create(item=item, size=size, rate=rate, thickness=thickness)
        
    customers = AddCustomer.objects.all()  
    return render(request, 'additem.html', {'customers': customers})
