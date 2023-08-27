from django.db import models
from apps.customers.models import Customer
from apps.invoice.models import SingleSalesInvoice
from apps.voucher.models import PurchaseInfo
from apps.vendors.models import Vendor
from apps.agency.models import Agency
# Create your models here.

class BankEntry(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE,blank=True, null=True)
    voucherId = models.ForeignKey(PurchaseInfo, on_delete=models.CASCADE, blank=True, null=True)
    vendorId = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
    InvoiceId = models.ForeignKey(SingleSalesInvoice, on_delete=models.CASCADE, blank=True, null=True)
    CustomerId = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    Post_Date = models.DateField()
    Value_Date = models.DateField()
    Name = models.CharField(max_length=100,  blank=True, null=True)
    Remitance_Branch = models.CharField(max_length=100,  blank=True, null=True)
    Total_Amount = models.CharField(max_length=100,  blank=True, null=True)
    Cheque_No = models.CharField(max_length=100,  blank=True, null=True) 
    GST_Type = models.CharField(max_length=100,  blank=True, null=True)
    Person_Type = models.CharField(max_length=100,  blank=True, null=True)
    Transaction_Type = models.CharField(max_length=100,  blank=True, null=True)
    Net_Balance_Paid = models.CharField(max_length=100,  blank=True, null=True)
    GST_Balance_Paid = models.CharField(max_length=100,  blank=True, null=True)
    Payment_Mode = models.CharField(max_length=100,  blank=True, null=True)
    Remarks = models.TextField(blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Date = models.DateField(auto_now = True)

    def __str__(self):
        return str(self.Name)