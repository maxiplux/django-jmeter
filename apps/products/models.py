from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=30)
    price = models.FloatField(default=100.0)

    def __str__(self):
        return  '{name} - {code}'.format(name=self.name, code=self.code)
