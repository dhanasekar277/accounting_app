from operator import mod
import re
from django.db import models
from apps.customers.models import PANNo, TINNo, CustomerPhoneNumber, CustomerGSTBillingAddress, Customer
from apps.purchase.models import PurchaseNetAmount, PurchaseRemainder
from apps.orders.models import MaterialOrder, Order
# Create your models here.

class Total(models.Model):
    cgst = models.CharField(max_length=100, blank=True)
    sgst = models.CharField(max_length=100, blank=True)
    roundedoff = models.CharField(max_length=100, blank=True)
    total = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.total

class CustomerInfo(models.Model):
    phone = models.ForeignKey(CustomerPhoneNumber, on_delete=models.CASCADE, blank=True)
    pan = models.ForeignKey(PANNo, on_delete=models.CASCADE, blank=True)
    tin = models.ForeignKey(TINNo, on_delete=models.CASCADE, blank=True)
    gst = models.ForeignKey(CustomerGSTBillingAddress, on_delete=models.CASCADE, blank=True)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return str(self.customerid)

class SalesMaterialInfo(models.Model):
    MatId = models.ForeignKey(MaterialOrder, on_delete=models.CASCADE, blank=True)
    Date = models.CharField(max_length=100, blank=True)
    CDC = models.CharField(max_length=100, blank=True)
    LDC = models.CharField(max_length=100, blank=True)
    Formula = models.CharField(max_length=100, blank=True)
    qty = models.CharField(max_length=100, blank=True)
    Moisture = models.CharField(max_length=100, blank=True)
    VehicleNo = models.CharField(max_length=100, blank=True)
    RoundOff = models.CharField(max_length=100, blank=True)
    Total = models.CharField(max_length=100, blank=True)
    WithGST = models.CharField(max_length=100, blank=True)
    SiteSupervisior = models.CharField(max_length=100, blank=True)
    QC = models.CharField(max_length=100, blank=True)
    Security = models.CharField(max_length=100, blank=True)
    Engineer = models.CharField(max_length=100, blank=True)
    DriverName = models.CharField(max_length=100, blank=True)
    UnloadingSupervisior = models.CharField(max_length=100, blank=True)
    orderId = models.CharField(max_length=100, blank=True)
    ig = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.MatId
  
class Sales(models.Model):
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, blank=True)
    poInfo = models.ManyToManyField(SalesMaterialInfo, blank=True)
    netAmount = models.ForeignKey(PurchaseNetAmount, on_delete=models.CASCADE, blank=True)
    remainder = models.ForeignKey(PurchaseRemainder, on_delete=models.CASCADE, blank=True)
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)
    sale_invoice = models.BooleanField(default=False)
    doc = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.customer)

class SalesCollection(models.Model):
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)
    sales = models.ManyToManyField(Sales, blank=True)

    def natural_key(self):
        data = []
        for i in self.sales.all():
            data.append({
                'WithGSTNetTotalAmount' : i.netAmount.WithGSTNetTotalAmount,
                'WithOutGSTNetTotalAmount' : i.netAmount.WithOutGSTNetTotalAmount,
                'AmountPayyed' : i.netAmount.AmountPayyed,
                'Balance' : i.netAmount.Balance,
                'Leggal_Name' : i.customer.gst.Leggal_Name,
                'Company_Name' : i.customer.customerid.Company_Name,
                'Trade_Name' : i.customer.gst.Trade_Name,
                'GST_No' : i.customer.gst.GST_No,
            })
        return data