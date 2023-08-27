from django.db import models
from apps.agency.models import Agency
# Create your models here.

class ExpenceCategories(models.Model):
    Agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True, blank=True)
    Category = models.CharField(max_length=100)

    def __str__(self):
        return self.Category

    def natural_key(self):
        return self.Category

class Assets(models.Model):
    Agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True, blank=True)
    Asset_Type = models.CharField(max_length=100)
    Asset_Name = models.CharField(max_length=100)
    Asset_Value = models.CharField(max_length=100)
    Date = models.DateField(auto_now=True)
    def __str__(self):
        return str(self.Asset_Name)


class Expences(models.Model):
    Agency = models.ForeignKey(Agency, on_delete=models.CASCADE,null=True, blank=True)
    Expence_Name = models.CharField(max_length=100)
    Expence_Category = models.ForeignKey(ExpenceCategories, on_delete=models.CASCADE)
    Payment_Mode = models.CharField(max_length=100)
    Payment_Type = models.CharField(max_length=100)
    Amount = models.CharField(max_length=100)
    Date = models.DateField()
    Bill_Reference = models.FileField(max_length=500, upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return str(self.Expence_Name)
    