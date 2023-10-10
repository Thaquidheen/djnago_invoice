
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('webapp.urls')),
    path('authentication/',include('authentication.urls')),
    path('additem/',include('additem.urls')),
    path('customer/',include('customer.urls')),
    path('stock/',include('stock.urls')),
    
]

