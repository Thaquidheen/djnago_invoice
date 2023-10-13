from django.shortcuts import render
from customer.models import AddCustomer
from additem.models import Item
# Create your views here.
def generateInvoice(request):
    customers = AddCustomer.objects.all()
    items = Item.objects.all()

    return render(request,'invoice.html',{'customers': customers, 'items': items})