from django.shortcuts import render
from customer.models import AddCustomer
from django.contrib.auth.decorators import login_required
from bill.models import InvoiceItem
from django.db.models import Sum
from django.template.loader import render_to_string

# Create your views here.


# def report(request):
#     customers = AddCustomer.objects.all()


#     customer_name = request.GET.get('customer_name')
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')   
#     invoice_items_query = InvoiceItem.objects.all()
#     customer_items = []
#     if customer_name:
#         invoice_items_query = invoice_items_query.filter(customer__customer_name=customer_name)
#     if start_date and end_date:
#         invoice_items_query = invoice_items_query.filter(invoice_date__range=(start_date, end_date))

#     items = invoice_items_query.filter(customer=customer)
#     total_amount = items.aggregate(Sum('amount'))['amount__sum'] or 0
#     customer_items.append({'customer_name': customer.customer_name, 'total_amount': total_amount})

#     customer_items = invoice_items_query
  
#     return render(request, 'report.html', {'customers': customers, 'customer_items': customer_items})


# def report(request):
#     customers = AddCustomer.objects.all()

#     customer_name = request.GET.get('customer_name')
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')   

#     customer_items = []

#     for customer in customers:
#         invoice_items_query = InvoiceItem.objects.all()

#         if customer_name:
#             invoice_items_query = invoice_items_query.filter(customer__customer_name=customer_name)
#         if start_date and end_date:
#             invoice_items_query = invoice_items_query.filter(invoice_date__range=(start_date, end_date))

#         items = invoice_items_query.filter(customer=customer)
#         total_amount = items.aggregate(Sum('amount'))['amount__sum'] or 0
#         customer_items.append({'customer_name': customer.customer_name, 'total_amount': total_amount})

#     return render(request, 'report.html', {'customers': customers, 'customer_items': customer_items})
@login_required
def report(request):
    customers = AddCustomer.objects.all()

    customer_name = request.GET.get('customer_name')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')   

    customer_items = []

    for customer in customers:
        invoice_items_query = InvoiceItem.objects.all().filter(customer=customer)
        print(invoice_items_query)
        if customer_name:
            invoice_items_query = invoice_items_query.filter(customer__customer_name=customer_name)
        if start_date and end_date:
            invoice_items_query = invoice_items_query.filter(invoice_date__range=(start_date, end_date))
        
        items = invoice_items_query.all()
        
        total_amount = items.aggregate(Sum('amount'))['amount__sum'] or 0

        customer_items.append({
            'customer_name': customer.customer_name,
            'total_amount': total_amount,
            'items': items
        })

    return render(request, 'report.html', {'customers': customers, 'customer_items': customer_items})
