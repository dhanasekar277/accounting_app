from sqlite3 import Timestamp
from django.db import models
from django.conf import settings
from django.db.models.enums import Choices
from apps.agency.models import Agency
from apps.vendors.models import Vendor,Material_Supplying
# Create your models here.

MATERIAL_TYPE = (
    ('N', 'Natural'),
    ('M', 'Manufactured')
)


# quality types
class ProductQuality(models.Model):
    Quality = models.CharField(max_length=100, null=True, blank=True)
    Price = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.Quality)


class LatestPrice(models.Model):
    Price = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.Price)


# Product models
class Product(models.Model):
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True)
    Product = models.CharField(max_length=100, blank=True)
    Material_Type = models.CharField(max_length=1, choices=MATERIAL_TYPE, default=1)
    Material_Supplying = models.ManyToManyField(Material_Supplying, blank=True)
    GST = models.CharField(max_length=20, blank=True, null=True)
    Ton = models.CharField(max_length=20, blank=True, null=True)
    HSNCode = models.CharField(max_length=20, blank=True, null=True)
    Quality = models.ManyToManyField(ProductQuality, blank=True)
    AvgPrice = models.CharField(max_length=20, blank=True)
    LatestPrice = models.ManyToManyField(LatestPrice, blank=True)
    Timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Product)