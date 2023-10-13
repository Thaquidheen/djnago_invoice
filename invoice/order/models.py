from django.db import models
from customer.models import AddCustomer
# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(AddCustomer, on_delete=models.CASCADE)
    order_date = models.DateField() 
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) 
    
    def __str__(self):
        return f"Order for {self.customer} on {self.order_date}"