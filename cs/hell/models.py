from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class categories(models.Model):
    catid = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=50,unique=True)
    #description=models.TextField()

class add_items(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=200)
    category = models.ForeignKey(categories,on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=200)
    quantity = models.IntegerField()
    actual_price = models.FloatField()
    discount_price = models.FloatField()
    image1 = models.FileField(upload_to='images')
    image2 = models.FileField(upload_to='images')
    image3 = models.FileField(upload_to='images')
    image4 = models.FileField(upload_to='images')
    updated_date=models.DateTimeField(default=datetime.now,blank=True)
    created_date=models.DateTimeField(default=datetime.now,blank=True)
    description=models.TextField(default="not specified")

class total(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tpurchase=models.FileField()

class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    itemname = models.ForeignKey(add_items,on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    @classmethod
    def get_total(self):
        return self.total_price*self.quantity

class useraddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField()
    pno = models.IntegerField()

class ordered_items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.IntegerField(primary_key=True, auto_created=True)
    order_item = models.ForeignKey(add_items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.now)
    payment_type = models.CharField(max_length=20, default="null")
    status = models.CharField(max_length=50, default="Payment pending")
    shipping_status = models.CharField(max_length=300, default="Shipping pending")
    delivery_status = models.CharField(max_length=300, default="Delivery pending")

class technician(models.Model):
    complaint_id = models.IntegerField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    contact = models.IntegerField()
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=100, default="Pending")
    complaint = models.TextField()

class wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    itemname = models.ForeignKey(add_items,on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    @classmethod
    def get_total(self):
        return self.total_price*self.quantity

class review(models.Model):
    itemname = models.ForeignKey(add_items,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    review = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    rating = models.IntegerField()

class contactdetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()