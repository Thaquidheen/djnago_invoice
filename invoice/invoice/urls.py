
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('webapp.urls')),
    path('authentication/',include('authentication.urls')),
    path('additem/',include('additem.urls')),
    path('customer/',include('customer.urls')),
    path('stock/',include('stock.urls')),
    path('invoice/',include('bill.urls')),
    path('report/',include('report.urls')),
    
]

