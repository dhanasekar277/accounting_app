from django.db import models
from apps.quotations.models import Quotation
from apps.purchase.models import PurchaseMaterialEntry
from apps.vendors.models import Vendor,VendorGST
from apps.agency.models import Signature
from apps.purchase.models import PurchaseEntry
# Create your models here.
SIGNATURE_CHOICES = (
    ('0', 'Prepared By'),
    ('1', 'Approved By'),
    ('2', 'Passed By'),
)

class VoucherVendorInfo(models.Model):
    Name = models.CharField(max_length=50, blank=True)
    AcNumber = models.CharField(max_length=50, blank=True)
    Bank = models.CharField(max_length=50, blank=True)
    IFSC = models.CharField(max_length=50, blank=True)
    Mobile = models.CharField(max_length=50, blank=True)
    GSTNo = models.ForeignKey(VendorGST, on_delete=models.CASCADE, null=True, blank=True)
    PanNo = models.CharField(max_length=50, blank=True)
    TradeName = models.CharField(max_length=50, blank=True)


class PurchaseInfo(models.Model):
    VoucherDate = models.CharField(max_length=50, blank=True)
    VoucherNo = models.CharField(max_length=50, blank=True)
    VoucherSLNo = models.CharField(max_length=50, blank=True)
    InvoiceNo = models.CharField(max_length=50, blank=True)
    DebitVoucherNo = models.CharField(max_length=50, blank=True)

    def _str_(self):
        return str(self.VoucherSLNo)



class VoucherSignature(models.Model):
    signature_name = models.CharField(choices=SIGNATURE_CHOICES, max_length=1, blank=True)
    signature_id = models.ForeignKey(Signature, on_delete=models.CASCADE)


class VourchersAmount(models.Model):
    total = models.CharField(max_length=50, blank=True)
    cgst_amount = models.CharField(max_length=50, blank=True)
    sgst_amount = models.CharField(max_length=50, blank=True)
    total_amount = models.CharField(max_length=50, blank=True)
    bank_entries = models.BooleanField(default=False)
    VoucherMaterialInfo = models.ManyToManyField(PurchaseMaterialEntry, blank=True) 
    Info = models.ForeignKey(PurchaseInfo, on_delete=models.CASCADE, blank=True, null=True)

    def natural_key(self):
        return ({
            'total_amount_withgst' : self.total_amount,
            'VoucherNo' : self.Info.VoucherNo,
            'voucher_date' : self.Info.VoucherDate,
            'total_withoutgst' : self.total,
            'cgst_amount' : self.cgst_amount,
            'sgst_amount' : self.sgst_amount,
        })


class VoucherDetail(models.Model):
    VendorId = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True)
    vendorDetail = models.ForeignKey(VoucherVendorInfo, on_delete=models.CASCADE, blank=True) 
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, blank=True) 
    amount = models.ManyToManyField(VourchersAmount, blank=True)
    signature = models.ManyToManyField(VoucherSignature, blank=True)
    Date = models.DateField(auto_now=True)

    def _str_(self):
        return str(self.VendorId)
    
    
class Voucher(models.Model):
    voucher = models.ManyToManyField(VoucherDetail, blank=True)
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, blank=True) 
    purchase = models.ForeignKey(PurchaseEntry, on_delete=models.CASCADE, blank=True)  
    Date = models.DateField(auto_now=True)
