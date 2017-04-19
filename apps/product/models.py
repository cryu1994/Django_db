from __future__ import unicode_literals
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=2255)
    weight =models.IntegerField()
    price = models.IntegerField()
    cost = models.IntegerField()
    category = models.CharField(max_length=225)
# Create your models here.
