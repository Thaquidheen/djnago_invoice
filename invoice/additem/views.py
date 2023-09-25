from django.shortcuts import render
from django.contrib import messages
from .models import item
# Create your views here.


def itempage(request):
    item_list = item.objects.all
    diction ={'items':item_list}
    return render(request,'itempage.html',context=diction)



def addItemform(request):
    if request.method == 'POST':
        item_name=request.POST.get('item_name')
        thickness=request.POST.get('thickness')
        size=request.POST.get('size')
        rate=request.POST.get('rate')
        
        addItemdata=item(item_name=item_name,thickness=thickness,size=size,rate=rate)
        addItemdata.save()
        messages.success(request, 'Item added successfully')
    return render(request,'additem.html')