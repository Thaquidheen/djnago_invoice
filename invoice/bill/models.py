from django.db import models
from customer.models import AddCustomer
from additem.models import Item


class InvoiceItem(models.Model):
    customer = models.ForeignKey(AddCustomer, on_delete=models.CASCADE) 
    invoice_date = models.DateField()
    invoice_number = models.CharField(max_length=255)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  
    thickness = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"InvoiceItem {self.item}"