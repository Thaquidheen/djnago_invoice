
from django.db import models
from customer.models import addcustomer


class Order(models.Model):
    customerid_id = models.ForeignKey(addcustomer, on_delete=models.CASCADE)
    OrderDate = models.DateField()
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order ID: {self.OrderID} - Customer: {self.customerid_id} - Date: {self.OrderDate}"