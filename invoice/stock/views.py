from django.shortcuts import render

# Create your views here.
def StockPage(request):
    return render(request,'stock.html')