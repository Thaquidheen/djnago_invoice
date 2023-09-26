

from django.db import models
from additem.models import item
from order.models import Order


class OrderItem(models.Model):
   
    Orderid_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    itemid_id = models.ForeignKey(item, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"OrderItem ID: {self.OrderItemID} - Order: {self.OrderID} - Item: {self.ItemID}"
