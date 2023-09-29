

from django.db import models
from additem.models import Item
from order.models import Order
from django.db.models.signals import pre_save
from django.dispatch import receiver



class OrderItems(models.Model):
    OrderItemID = models.AutoField(primary_key=True)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_Amount(self):
        if self.Item is not None:
            self.Amount= self.Quantity * self.Item.rate

    def __str__(self):
        return f"OrderItem ID: {self.OrderItemID}, Order: {self.Order}, Item: {self.Item}, Quantity: {self.Quantity}, Subtotal: {self.Amount}"


@receiver(pre_save, sender=OrderItems)
def update_orderitem_Amount(sender, instance, **kwargs):
    instance.calculate_Amount()
