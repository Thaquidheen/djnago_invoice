from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.
class item(models.Model):
    item_name= models.CharField(max_length=600,blank=False)
    thickness = models.CharField(max_length=50,blank=False)  
    size = models.CharField(max_length=50,blank=False) 
    rate = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')  

    def __str__(self):
        return self.item_name
