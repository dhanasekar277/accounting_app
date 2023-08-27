from django.db import models
from django.conf import settings
from apps.agency.models import Agency
from apps.vendors.models import Vendor
from apps.products.models import Product
from apps.customers.models import Customer, CustomerDeliveryAddress
# Create your models here.

StatusUnloading = [
    ('I', 'Initiator'),
    ('O', 'On Hold'),
    ('D', 'Delivered')
]


PO_TYPES = (
    ('PA', 'PO Applicable'),
    ('NA', 'Not Applicable')
)

MATERIAL_TYPE = (
    ('N', 'Natural'),
    ('M', 'Manufactured')
)

MOISTURE_TYPE = (
    ('1', 'Yes'),
    ('0', 'No')
)

QUANTITY_TYPE = (
    ('0', 'NO'),
    ('1', 'MT'),
    ('2', 'CFT'),
    ('4', 'QF'),
    ('5', 'M3'),
    ('6', 'QM'),
    ('7', 'Cage'),
    ('8', 'KG'),
)

 
"""PO Material Info"""
class POMaterialInfo(models.Model):
    Material_Name = models.CharField(max_length=100, blank=True, null=True)
    Material_Id = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    Quantity = models.CharField(max_length=10, blank=True, null=True)
    Quantity_Type = models.CharField(choices=QUANTITY_TYPE, default=0, max_length=1)
    Load = models.CharField(max_length=20, blank=True, null=True)
    PO_Rate = models.CharField(max_length=50, blank=True, null=True)
    Moisture = models.CharField(choices=MOISTURE_TYPE, max_length=1, default=0)
    Moisture_No = models.CharField(max_length=30, default=0)
    PO_Terms = models.CharField(max_length=100, blank=True, null=True)
    Published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}'.format(self.Material_Name)


""" Po number Models"""
class PONumber(models.Model): 
    PO_Type = models.CharField(choices=PO_TYPES, max_length=2) 
    PO_Number = models.CharField(max_length=100, blank=True, null=True) 
    Scan_Copy = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)
    PO_Reciver_Name = models.CharField(max_length=50, blank=True, null=True)
    PO_Reciver_Mail = models.CharField(max_length=50, blank=True, null=True)
    PO_Approved_By = models.CharField(max_length=50, blank=True, null=True)
    PO_Material_Info = models.ManyToManyField(POMaterialInfo, blank=True)
    PO_Date = models.DateField(blank=True, null=True)
    Order_Recieved_Date = models.DateField(blank=True, null=True)
    Order_Expected_Date = models.DateField(blank=True, null=True)
    Remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.PO_Type)

   
""" Material order list """
class MaterialOrder(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    Vendor_Type = models.CharField(max_length=100, blank=True, null=True)
    Location_Supply = models.CharField(max_length=100, blank=True, null=True)
    Delivery_Site = models.CharField(max_length=100, default="AT SITE", blank=True, null=True)
    Payment_Capability = models.CharField(max_length=100, blank=True, null=True)
    Mat_PO_ID = models.ForeignKey(POMaterialInfo, on_delete=models.CASCADE)
    Product_Name = models.ForeignKey(Product, on_delete=models.CASCADE)
    Material_Name = models.CharField(max_length=100, blank=True, null=True)
    Expected_Date = models.DateField()
    Quantity = models.CharField(max_length=50, blank=True, null=True)
    Quantity_Type = models.CharField(max_length=1,choices=QUANTITY_TYPE,default=0, blank=True, null=True)#
    Load = models.CharField(max_length=50, blank=True, null=True)
    Current_Price = models.CharField(max_length=50, blank=True, null=True)
    Sale_Price = models.CharField(max_length=50, blank=True, null=True)
    Purchase_Price = models.CharField(max_length=50, blank=True, null=True)
    Fianl_PO_Price = models.CharField(max_length=50, blank=True, null=True)
    Final_Purchase_Price = models.CharField(max_length=50, blank=True, null=True)
    Final_Offer_Price = models.CharField(max_length=50, blank=True, null=True)
    HSNCode = models.CharField(max_length=50, blank=True, null=True)
    Quality_Material_Type = models.CharField(max_length=1, choices=MATERIAL_TYPE, default=1, blank=True, null=True)
    Moisture = models.CharField(max_length=1, choices=MOISTURE_TYPE, default=1, blank=True, null=True)
    Moisture_Number = models.CharField(max_length=50, blank=True, null=True)
    Purchase_Entry = models.BooleanField(default=False)
    Sale_Entry = models.BooleanField(default=False)
    Material_Term = models.CharField(max_length=100, blank=True, null=True)
    Others = models.TextField(blank=True, null=True)

    def __str__(self):
       return '{0}'.format(self.Material_Name)

 
""" Daily Order Info """
class Order(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    Sales_Company = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Sales_Delivery_Address = models.TextField()	
    Billing_Address = models.TextField()		
    PO_Number = models.ForeignKey(PONumber, on_delete=models.CASCADE)
    Materials = models.ManyToManyField(MaterialOrder)
    Approved = models.BooleanField(default=False)
    SalesApproved = models.BooleanField(default=False)
    Date = models.DateField(auto_now = True)
    def __str__(self):
       return str(self.Billing_Address)

