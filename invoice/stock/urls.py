from django.urls import path
from . import views 

urlpatterns = [
    path('', views.StockPage, name='addstock'),
]