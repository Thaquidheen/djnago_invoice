from django.shortcuts import render
from django.http import JsonResponse
from .models import  InvoiceItem
from customer.models import AddCustomer
from additem.models import *
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory
from decimal import Decimal 
from django.contrib.auth.decorators import login_required

@login_required
def generateInvoice(request):
    customers = AddCustomer.objects.all()
    
    if request.method == 'POST':
        item_count = int(request.POST.get('item-count'))
        
        for i in range(1, item_count + 1):
            customer_name = request.POST.get('customer')
            invoice_date = request.POST.get('invoice-date')
            invoice_number = request.POST.get('invoice-number')
            items = request.POST.getlist(f'item-{i}')  
            thickness = Decimal(request.POST.get(f'thickness-{i}'))
            sizes = request.POST.getlist(f'size-{i}')
            quantities = request.POST.getlist(f'quantity-{i}')
            areas = request.POST.getlist(f'area-{i}')
            rates = request.POST.getlist(f'rate-{i}')
            amounts = request.POST.getlist(f'amount-{i}')
            
            customer = AddCustomer.objects.get(customer_name=customer_name)
            
 
            for item, size, quantity, area, rate, amount in zip(items, sizes, quantities, areas, rates, amounts):
                item = Item.objects.get(pk=item)
                invoice_item = InvoiceItem(
                    customer=customer,
                    invoice_date=invoice_date,
                    invoice_number=invoice_number,
                    item=item,
                    thickness=thickness,
                    size=size,
                    quantity=Decimal(quantity),
                    area=Decimal(area),
                    rate=Decimal(rate),
                    amount=Decimal(amount)
                )
                invoice_item.save()
                print(f'Customer Name: {customer_name}')
                print(f'Invoice Date: {invoice_date}')
                print(f'Invoice Number: {invoice_number}')
                print(f'Items: {items}')

    return render(request, 'invoice.html', {'customers': customers})





def get_items(request):
    items = Item.objects.all()
    item_data = []
    
    for item in items:
        item_variations = ItemVariation.objects.filter(item=item)
        item_data.append({
            'id': item.id,
            'item_name': item.item_name,
            'variations': [{'size': var.size, 'thickness': var.thickness, 'rate': var.rate} for var in item_variations]
        })
    
    data = {'items': item_data}
    return JsonResponse(data, safe=False)