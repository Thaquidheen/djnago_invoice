from django.shortcuts import render
from customer.models import AddCustomer
from django.contrib.auth.decorators import login_required
from bill.models import InvoiceItem
# Create your views here.


@login_required
def report(request):
    customers = AddCustomer.objects.all()


    customer_name = request.GET.get('customer_name')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')   
    invoice_items_query = InvoiceItem.objects.all()

    if customer_name:
        invoice_items_query = invoice_items_query.filter(customer__customer_name=customer_name)
    if start_date and end_date:
        invoice_items_query = invoice_items_query.filter(invoice_date__range=(start_date, end_date))


    # customer_items = InvoiceItem.objects.filter(customer__customer_name=customer_name)
    # date_range_items = InvoiceItem.objects.filter(invoice_date__range=(start_date, end_date))
    customer_items = invoice_items_query
    print(customer_items)
    print("Start Date:", start_date)
    print("End Date:", end_date)
    # print(date_range_items)
    return render(request, 'report.html', {'customers': customers, 'customer_items': customer_items})
