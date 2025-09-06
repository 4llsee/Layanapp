from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    icon=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name
    

class Cosutmer(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=50)

class Products(models.Model):
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=6)
    storage=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    image=models.ImageField(upload_to='mobile/images')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
       return self.name
    

class Cart(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
   session_id=models.CharField(max_length=100,null=True,blank=True)
   product=models.ForeignKey(Products,on_delete=models.CASCADE)
   quntity=models.PositiveBigIntegerField(default=0)
   created_at=models.DateTimeField(auto_now_add=True)

class PaymentCard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=120)
    last4 = models.CharField(max_length=4)
    expiry = models.CharField(max_length=5)  # MM/YY
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cardholder_name} ••••{self.last4} ({self.expiry})"
    

    # 1) طلب وفقراته
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment = models.ForeignKey('PaymentCard', on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, default='paid')  # أو 'pending'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user}"
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.PROTECT)  # غيّري الاسم لو موديلك مختلف
    quntity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # سعر وقت الشراء

    def __str__(self):
        return f"{self.product} x{self.quantity}"
   