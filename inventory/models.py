from django.db import models

# Create your models here.

class Inventory(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="%Y%m%d")
    desc = models.TextField()
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=20)
    opponent = models.CharField(max_length=30)

class Opponent(models.Model):
    name = models.CharField(max_length=30)
    tel = models.CharField(max_length=40)
    address = models.CharField(max_length=140)