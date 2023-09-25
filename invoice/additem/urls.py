from django.urls import path
from . import views

urlpatterns = [
    path('', views.addItemform, name='additem'),
    path('items/', views.itempage, name='items'),
]