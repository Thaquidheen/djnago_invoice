from django.db import models
from fractions import Fraction
from customer.models import AddCustomer

class FractionField(models.Field):
    description = "A field for storing fractions"

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return Fraction(value)

    def to_python(self, value):
        if isinstance(value, Fraction):
            return value
        if value is None:
            return None
        return Fraction(value)

    def get_prep_value(self, value):
        if value is None:
            return None
        return float(value)

    def get_internal_type(self):
        return 'DecimalField'

    def get_db_prep_save(self, value, connection):
        return float(value)
class Item(models.Model):
    item_name = models.CharField(max_length=255) 
    
    def __str__(self):
        return self.item_name

class ItemVariation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  
    size = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits=10, decimal_places=2)  
    thickness = models.DecimalField(max_digits=6, decimal_places=2)  


    def __str__(self):
        return f"{self.item.item_name} - Size: {self.size}, Rate: {self.rate}, Thickness: {self.thickness}"