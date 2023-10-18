from django.urls import path
from . import views

urlpatterns = [
    path('', views.generateInvoice, name='invoicegenerate'),
    path('get_items/', views.get_items, name='get_items'),
]
