from typing import Any
from django.db import models

# Create your models here.


class addcustomer(models.Model):
    customer_name = models.CharField(max_length=100,blank=False)
    customer_number = models.CharField(max_length=200,blank=False)


    def __str__(self):
        return self.customer_name

