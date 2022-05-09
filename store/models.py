import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cetagory(models.Model):
    name=models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Sub_Cetagory(models.Model):
    name = models.CharField(max_length=70)
    cetagory = models.ForeignKey(Cetagory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Brand(models.Model):
    name=models.CharField(max_length=70,)

    def __str__(self):
        return self.name

class contact_us(models.Model):
    name= models.CharField(max_length=70)
    email= models.CharField(max_length=70)
    subject=models.CharField(max_length=70)
    message=models.CharField(max_length=70)



class Product(models.Model):
    Availability = (('In the stock','In the stock'),('out the stock ','Out the Stock'))
    cetagory = models.ForeignKey( Cetagory,on_delete=models.CASCADE,null=False,default='')
    sub_cetagory = models.ForeignKey(Sub_Cetagory,on_delete=models.CASCADE,null=False,default='')
    Brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,default='')
    image = models.ImageField(upload_to='ecommerce/pimg')
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    Availability =models.CharField(choices=Availability,null=True,max_length=70)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    image=models.ImageField(upload_to='ecommerce/pimg/')
    product=models.CharField(max_length=70)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    quantity=models.CharField(max_length=70)
    price = models.FloatField(max_length=70)
    address= models.TextField(null=True,blank=True)
    phone = models.CharField(max_length=70,default='')
    pincode = models.CharField(max_length=70,null=True,blank=True)
    total = models.CharField(max_length=70,default='')
    date = models.DateTimeField(default=datetime.datetime.today)
