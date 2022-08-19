from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
from apps.products.models import Product


class Order(models.Model):
    created_at = models.DateField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT)


class OrderLine(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.FloatField(default=0.0)