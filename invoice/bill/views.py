from django.shortcuts import render
from django.http import JsonResponse
from .models import  InvoiceItem
from customer.models import AddCustomer
from additem.models import *
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory
from decimal import Decimal 


def generateInvoice(request):

    customers = AddCustomer.objects.all()
    if request.method == 'POST':
        customer_name = request.POST.get('customer')
        invoice_date = request.POST.get('invoice-date')
        invoice_number = request.POST.get('invoice-number')
        item_count = int(request.POST.get('item-count'))


        for i in range(1, item_count + 1):
            item_id = request.POST.get('item')
            thickness = Decimal(request.POST.get('thickness'))
            size = request.POST.get('size')
            quantity = Decimal(request.POST.get('quantity'))
            area = Decimal(request.POST.get('area'))
            rate = Decimal(request.POST.get('rate'))
            amount = Decimal(request.POST.get('amount'))

            customer = AddCustomer.objects.get(customer_name=customer_name)
            item = Item.objects.get(pk=item_id)


       
            invoice_item = InvoiceItem(
                customer=customer,
                invoice_date=invoice_date,
                invoice_number=invoice_number,
                item=item,
                thickness=thickness,
                size=size,
                quantity=quantity,
                area=area,
                rate=rate,
                amount=amount
             )
            invoice_item.save()

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