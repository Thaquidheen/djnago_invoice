from django.db import models

# Create your models here.


class AddCustomer(models.Model):
     

     customer_name= models.CharField(max_length=600,blank=False)

   
     def __str__(self):
        return self.customer_name