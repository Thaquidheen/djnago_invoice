from django.shortcuts import render
from django.http import JsonResponse

from customer.models import AddCustomer
from additem.models import *
# Create your views here.
def generateInvoice(request):
    customers = AddCustomer.objects.all()
    items = Item.objects.all()


    return render(request,'invoice.html', {'customers': customers, 'items': items, })


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