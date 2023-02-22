from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class regmodel(models.Model):
#     name=models.CharField(max_length=30)
#     email=models.EmailField()
#     phone=models.IntegerField()
#     address=models.CharField(max_length=100)
#     pincode=models.IntegerField()
#     password=models.CharField(max_length=20)

class regmodel(models.Model):
    username=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username

class regsellermodel(models.Model):
    sname=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    pincode=models.IntegerField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.sname


class filemodel(models.Model):
    shopid=models.IntegerField()
    pname=models.CharField(max_length=40)
    pprize=models.IntegerField()
    pdes=models.CharField(max_length=100)
    pimage=models.ImageField(upload_to='myapp/static')
    def __str__(self):
        return self.pname



class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user


class cart(models.Model):
    pname=models.CharField(max_length=40)
    pprize=models.IntegerField()
    pdes=models.CharField(max_length=100)
    pimage=models.ImageField()
    def __str__(self):
        return self.pname

class wishlist(models.Model):
    pname=models.CharField(max_length=40)
    pprize = models.IntegerField()
    pdes = models.CharField(max_length=100)
    pimage = models.ImageField()
    def __str__(self):
        return self.pname

class buy(models.Model):
    pname=models.CharField(max_length=40)
    pprize = models.IntegerField()
    pdes = models.CharField(max_length=100)
    pimage = models.ImageField()
    quantity=models.IntegerField()

class buy1(models.Model):
    pname=models.CharField(max_length=40)
    pprize = models.IntegerField()
    pdes = models.CharField(max_length=100)
    quantity=models.IntegerField()
    def __str__(self):
        return self.pname

class customercard(models.Model):
    cardname=models.CharField(max_length=30)
    cardnumber=models.CharField(max_length=30)
    cardexpiry=models.CharField(max_length=30)
    securitycode=models.CharField(max_length=30)
    def __str__(self):
        return self.cardname