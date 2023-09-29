from django.urls import path
from . import views

urlpatterns = [
    path('', views.addItemform, name='additem'),
    path('items/<int:customer_id>/', views.itempage, name='items'),
]