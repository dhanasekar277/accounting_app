from django.db import models
from apps.agency.models import AgencyBankAccount, AgencyPhone
from apps.orders.models import Order
from apps.sales.models import Sales, SalesMaterialInfo, SalesCollection

# Create your models here.


class DCDetail(models.Model):
    material_name = models.CharField(max_length=100, blank=True)
    dcNo = models.CharField(max_length=100, blank=True)
    dcdate = models.CharField(max_length=100, blank=True)
    hsc = models.CharField(max_length=100, blank=True)
    quantity = models.CharField(max_length=100, blank=True)
    rate = models.CharField(max_length=100, blank=True)
    per = models.CharField(max_length=100, blank=True)
    amount = models.CharField(max_length=100, blank=True)

    def _str_(self):
        return str(self.material_name)
 

class SingleSalesInvoice(models.Model):
    InvoiceNo = models.CharField(max_length=100, blank=True)
    InvoiceDate = models.CharField(max_length=100, blank=True)
    DeliveryNote = models.CharField(max_length=100, blank=True)
    OtherReference = models.CharField(max_length=100, blank=True)
    SupplierRef = models.CharField(max_length=100, blank=True)
    TermsPayment = models.CharField(max_length=100, blank=True)
    DeliveryNote = models.CharField(max_length=100, blank=True)
    Destination = models.CharField(max_length=100, blank=True)
    DespatchDocumentNo = models.CharField(max_length=100, blank=True)
    BankAccount = models.ForeignKey(
        AgencyBankAccount, on_delete=models.CASCADE, blank=True
    )
    DC = models.ManyToManyField(DCDetail, blank=True)
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)
    phone = models.ForeignKey(AgencyPhone, on_delete=models.CASCADE, blank=True)
    saleid = models.ForeignKey(Sales, on_delete=models.CASCADE, blank=True)

    def _str_(self):
        return str(self.InvoiceNo)

    def natural_key(self):
        data = []
        dic = {
            "InvoiceNo": self.InvoiceNo,
            "InvoiceDate": self.InvoiceDate,
        }
        for i in self.orderid.Materials.all():
            dic["HSNCode"] = i.Product_Name.HSNCode,
            dic["GST"] = i.Product_Name.GST,
            break
        data.append(dic)
        return data


class SalesInvoice(models.Model):
    saleid = models.ForeignKey(SalesCollection, on_delete=models.CASCADE, blank=True)
    invoice = models.ManyToManyField(SingleSalesInvoice, blank=True)
    Date = models.DateField(auto_now=True)
