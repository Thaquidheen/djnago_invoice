
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('authentication/',include('authentication.urls')),
    path('stocks/',include('stocks.urls')),
    path('additem/',include('additem.urls')),
    path('addcustomer/',include('customer.urls')),
    path('order/',include('order.urls')),
]

