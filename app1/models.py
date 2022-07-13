from django.db import models
import datetime
from django.utils import timezone



# Create your models here.

class Person(models.Model):
    text=models.CharField(max_length=200)
    date=models.DateTimeField('date')

    def __str__(self):
        return self.text
    def publier(self):
        return self.date >=timezone.now() - datetime.timedelta(day=1)


class Profile(models.Model):
    name=models.CharField(max_length=350)
    productID=models.CharField(max_length=350)
    description = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    number = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name

    def infosProfile(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=350)
    productID = models.CharField(max_length=350)
    price = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    img=models.CharField(max_length=1000)

    def __str__(self):
        return self.productID

    def infosProfile(self):
        return self.productID
