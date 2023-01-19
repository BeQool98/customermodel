from django.db import models
from django.contrib.auth.models import User
from mystore.models import StoreProduct

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True, blank = True)
    email = models.CharField(max_length = 200,  null = True)
    profile_pic = models.ImageField(default = "profile2.png", null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    
 
'''    
class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'), 
        ('Out Door', 'Out Door')
    )
    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length = 200,  null = True, choices = CATEGORY)
    description = models.CharField(max_length = 200,  null = True, blank  = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name
    '''
    
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'), 
        ('Out for Delivery', 'Out for Delivery'), 
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    status = models.CharField(max_length = 200, null = True, choices = STATUS)
    notes = models.CharField(max_length = 1000, null = True, blank = True)
    complete = models.BooleanField(default = False, null = True, blank = True)
    
    def __str__(self):
        return self.customer.name + 's'  + ' ' + "Order"
    
    
    
    
class OrderItem(models.Model):  
     order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True, blank = True)
     products = models.ForeignKey(StoreProduct, null = True, blank = True,  on_delete = models.SET_NULL)
     price = models.DecimalField(max_digits = 8, decimal_places = 2, null = True, blank = True)
     quantity = models.IntegerField(default = 0, null = True, blank = True)
     
     def __str__(self):
         return self.products.name
     
     
    
   
    