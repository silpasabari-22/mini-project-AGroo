from django.db import models
from django.contrib.auth.models import AbstractUser

class Customuser(AbstractUser):
    users = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


    def __str__(self):
        return self.username



class Product(models.Model):
    farmer_id=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    product_category=models.CharField(max_length=100)
    product_image=models.ImageField()
    quantity=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user_id=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField()

    def __str__(self):
        return f"Cart of {self.user_id.username}"