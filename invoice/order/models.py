
from django.db import models
from customer.models import AddCustomer


class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    Customer = models.ForeignKey(AddCustomer, on_delete=models.CASCADE)  
    OrderDate = models.DateField()
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Order ID: {self.OrderID}, Customer: {self.Customer}, Date: {self.OrderDate}, Total Amount: {self.TotalAmount}"