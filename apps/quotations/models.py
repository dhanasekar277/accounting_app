from django.db import models
from apps.customers.models import Customer
from apps.agency.models import Agency
from apps.orders.models import MaterialOrder, PONumber, Order, POMaterialInfo
# Create your models here.


class PurchaseQuotation(models.Model):  
    material = models.ManyToManyField(MaterialOrder, blank=True)
    published = models.DateTimeField(auto_now_add=True)


class SalesQuotation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    po = models.ForeignKey(PONumber, on_delete=models.CASCADE)
    po_materials = models.ManyToManyField(POMaterialInfo, blank=True)
    published = models.DateTimeField(auto_now_add=True)
 

class CustomerQuotationDetail(models.Model):
    customerName = models.CharField(max_length=100, blank=True)
    customerCompany = models.CharField(max_length=100, blank=True)
    customerAddress = models.CharField(max_length=100, blank=True)
    customerPosition = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.customerName)


class CustomerQuotationTerms(models.Model):
    detail = models.ForeignKey(CustomerQuotationDetail, on_delete = models.CASCADE, blank=True, null=True)
    advance = models.CharField(max_length=100, blank=True)
    days = models.CharField(max_length=100, blank=True)
    generateDate = models.CharField(max_length=100, blank=True)
    gstType = models.CharField(max_length=50, blank=True)
    NonGstTerms = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.gstType)

 
class VendorQuotationDetail(models.Model):
    date = models.CharField(max_length=100, blank=True)
    mat_id = models.ManyToManyField(MaterialOrder, blank=True)
    VendorGstTerms = models.TextField(blank=True, null=True)
    # purchaseGenerated = models.BooleanField(default=False)
    #purchase id
    def __str__(self) :
        return self.date


class Quotation(models.Model):
    agency = models.ForeignKey(Agency, on_delete = models.CASCADE)
    purchase = models.ForeignKey(PurchaseQuotation, on_delete = models.CASCADE)
    sales = models.ForeignKey(SalesQuotation, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    customerGenerate = models.BooleanField(default=False)
    customerInfo = models.ForeignKey(CustomerQuotationTerms, on_delete=models.CASCADE, blank=True, null=True)
    vendorGenerate = models.BooleanField(default=False)
    vendorInfo = models.ManyToManyField(VendorQuotationDetail, blank=True)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.agency)

    def natural_key(self):
        data = []
        for i in self.order.Materials.all():
            data.append({
                'hsncode' : i.Product_Name.HSNCode,
                'gst' : i.Product_Name.GST
            })
            break
        return data
