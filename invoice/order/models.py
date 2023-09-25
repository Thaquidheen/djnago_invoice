from django.db import models
from customer.models import AddCustomer 
# Create your models here.

class Order(models.Model):
    order_id = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(AddCustomer, on_delete=models.CASCADE)  
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_id