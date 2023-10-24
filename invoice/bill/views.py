from django.shortcuts import render
from django.http import JsonResponse
from .models import  InvoiceItem
from customer.models import AddCustomer
from additem.models import *
# Create your views here.
def generateInvoice(request):
    customers = AddCustomer.objects.all()
    
    try:
        if request.method == 'POST':
            customer = request.POST['customer']
            invoice_date = request.POST['invoice-date']
            invoice_number = request.POST['invoice-number']
            items = []

            for i in range(1, int(request.POST['item-count']) + 1):
                item_id = request.POST.get(f'item-{i}')
                thickness = request.POST.get(f'thickness-{i}')
                size = request.POST.get(f'size-{i}')
                quantity = request.POST.get(f'quantity-{i}')
                area = request.POST.get(f'area-{i}')
                rate = request.POST.get(f'rate-{i}')
                amount = request.POST.get(f'amount-{i}')

                items.append(InvoiceItem(
                    customer=customer,
                    invoice_date=invoice_date,
                    invoice_number=invoice_number,
                    item_id=item_id,
                    thickness=thickness,
                    size=size,
                    quantity=quantity,
                    area=area,
                    rate=rate,
                    amount=amount,
                ))

            InvoiceItem.objects.bulk_create(items)
      
    except KeyError as e:
        print(f"Error: {e}")
    
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