from django.db import models

# Create your models here.


class Product(models.Model):
  type = models.CharField(max_length=255)
  flavor= models.CharField(max_length=255)
  price = models.FloatField()
  stock = models.IntegerField()
  image = models.CharField(max_length=25500)
