from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Item
from django.urls import reverse
from customer.models import AddCustomer
 # Create your views here.


def itempage(request,customer_id):
    print("Customer ID:", customer_id) 
    customer = get_object_or_404(AddCustomer, pk=customer_id)
    item_list = Item.objects.filter(customer=customer)
    print(item_list)
    diction ={'customer':customer,'items':item_list}
    return render(request,'itempage.html',context=diction)



def addItemform(request):
    customers = AddCustomer.objects.all()
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        print(customer_id)
        try:
            customer = AddCustomer.objects.get(pk=customer_id)
            print("Selected Customer:", customer)
        except AddCustomer.DoesNotExist:
            messages.error(request, 'Selected customer does not exist.')
            return redirect('additem')
        
        item_name=request.POST.get('item_name')
        thickness=request.POST.get('thickness')
        size=request.POST.get('size')
        rate=request.POST.get('rate')
        print("Item Name:", item_name)
        item_data = Item(item_name=item_name, thickness=thickness, size=size, rate=rate, customer=customer)
        item_data.save()
        messages.success(request, 'Item added successfully')
        # show_all_items_url = reverse('items', args=[customer_id])
        # return render(request, 'additem.html', {'customers': customers, 'show_all_items_url': show_all_items_url})
        return redirect('items', customer_id=customer_id)
        
    return render(request,'additem.html', {'customers': customers})