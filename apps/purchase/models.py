from django.db import models
from apps.customers.models import Customer
from apps.vendors.models import Vendor
from apps.orders.models import Order, MaterialOrder
from apps.quotations.models import Quotation
# Create your models here. 

class PurchaseMaterialEntry(models.Model):
    p_id = models.CharField(max_length=10, blank=True)
    mat_id = models.ForeignKey(MaterialOrder, on_delete = models.CASCADE, blank=True)
    PurchaseDate = models.CharField(max_length=50, blank=True)
    Site = models.CharField(max_length=50, blank=True)
    UnloadingSite = models.CharField(max_length=50, blank=True)
    MaterialName = models.CharField(max_length=50, blank=True)
    CDC = models.CharField(max_length=50, blank=True, null=True)
    LDC = models.CharField(max_length=50, blank=True, null=True)
    VehicleNo = models.CharField(max_length=50, blank=True, null=True) #mis
    Moisture = models.CharField(max_length=50, blank=True, null=True)
    QuantityType = models.CharField(max_length=50, blank=True, null=True)
    QtyFormula = models.CharField(max_length=50, blank=True, null=True)
    QtyCalc = models.CharField(max_length=50, blank=True, null=True)
    RoundOff = models.CharField(max_length=50, blank=True, null=True)
    Rate = models.CharField(max_length=50, blank=True, null=True)
    Total = models.CharField(max_length=50, blank=True, null=True) 
    M3Cft = models.CharField(max_length=50, blank=True, null=True)
    M3Ton = models.CharField(max_length=50, blank=True, null=True)
    GST = models.CharField(max_length=50, blank=True, null=True)
    WithGST = models.CharField(max_length=50, blank=True, null=True)
    SiteSupervisior = models.CharField(max_length=50, blank=True, null=True)
    QC = models.CharField(max_length=50, blank=True, null=True)
    Security = models.CharField(max_length=50, blank=True, null=True)
    Engineer = models.CharField(max_length=50, blank=True, null=True)
    DriverName = models.CharField(max_length=50, blank=True, null=True)
    UnloadingSupervisior = models.CharField(max_length=50, blank=True, null=True)
    ig = models.BooleanField(default=False)

    def __str__(self):
        return str(self.MaterialName)
 

class PurchaseRemainder(models.Model):
    GSTFilledInvNo = models.CharField(max_length=50, blank=True)
    GSTFilledScanCopy = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)
    GSTFilledInvReceive = models.CharField(max_length=50, blank=True)
    GSTFilledFiledCheck = models.CharField(max_length=2, blank=True)


class PurchaseNetAmount(models.Model):
    WithOutGSTNetTotalAmount = models.CharField(max_length=50, blank=True)
    WithGSTNetTotalAmount = models.CharField(max_length=50, blank=True)
    AmountPayyed = models.CharField(max_length=50, blank=True)
    Balance = models.CharField(max_length=50, blank=True)
    GstTotal = models.CharField(max_length=50, blank=True)
    GstPayyed = models.CharField(max_length=50, blank=True)
    GstBalance = models.CharField(max_length=50, blank=True) 


class purchaseInvoice(models.Model):
    gstNo = models.CharField(max_length=50, blank=True)
    phNo = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=10, blank=True)


class SinglePurchaseEntry(models.Model):
    vendorId = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    customerId = models.ForeignKey(Customer, on_delete = models.CASCADE)
    purchaseMaterial = models.ManyToManyField(PurchaseMaterialEntry, blank=True)
    remainder = models.ForeignKey(PurchaseRemainder, on_delete=models.CASCADE)
    netAmount = models.ForeignKey(PurchaseNetAmount, on_delete=models.CASCADE, blank=True)
    quotation = models.ForeignKey(Quotation, on_delete = models.CASCADE)
    invoice = models.ForeignKey(purchaseInvoice, on_delete = models.CASCADE, blank=True, null=True)
    doc = models.DateTimeField(auto_now=True)
 
class PurchaseEntry(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete = models.CASCADE)
    vendorId = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    entries = models.ManyToManyField(SinglePurchaseEntry, blank=True)
    doc = models.DateTimeField(auto_now_add=True)

    