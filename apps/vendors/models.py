from django.db import models
from django.conf import settings
from django.http import HttpResponse
from apps.agency.models import Agency
from django.utils import timezone

# from server.agencies.apps.customers.models import Branch
# Create your models here.

GST_TYPE_CHOICES =(
    ("0", "GST User"),
    ("1", "Unregistered User"),
)

MATERIAL_CHOICES =(
    ("N", "Natural"),
    ("M", "Manufactured"),
)

VENDOR_CATEGORY_CHOICES =(
    ("Q", "Quarry Owner"),
    ("T", "Transport Owner"),
    ("C", "Crusher Owner"),
)



""" Vendor GST BANK """
class VendorGSTBankAccount(models.Model):
    Address = models.CharField(max_length=50,null=True, blank=True)
    City = models.CharField(max_length=50,null=True, blank=True)
    State = models.CharField(max_length=50,null=True, blank=True)
    Zip = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.Address)

 
""" Vendor Certificate """
class VendorCertificate(models.Model):
    Vendor_Certificate_Name = models.CharField(max_length=100, blank=True, null=True)
    Vendor_Certificate_Scan_Copy = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self) :
        return '{0}'.format(self.Vendor_Certificate_Name)


""" Vendor Tin No """
class VendorTIN(models.Model):
    TIN_No = models.CharField(max_length=100, blank=True, null=True)
    TIN_Scan_Copy = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self) :
        return '{0}'.format(self.TIN_No)


""" Vendor PAN """
class VendorPAN(models.Model):
    PAN_No = models.CharField(max_length=100, blank=True, null=True)
    PAN_Scan_Copy = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self) :
        return '{0}'.format(self.PAN_No)


"""Vendor GST"""
class VendorGST(models.Model):
    Leggal_Name = models.CharField(max_length=50, blank=True, null=True)
    Trade_Name = models.CharField(max_length=50, blank=True, null=True)
    Holder_Name = models.CharField(max_length=50, blank=True, null=True)
    GST_No = models.CharField(max_length=50, blank=True, null=True)
    Phone = models.CharField(max_length=20, blank=True, null=True)
    Name = models.CharField(max_length=40, blank=True, null=True)
    Email = models.CharField(max_length=40, blank=True, null=True)
    Bank_Account = models.CharField(max_length=40, blank=True, null=True)
    Account_Number = models.CharField(max_length=40, blank=True, null=True)
    IFSC = models.CharField(max_length=40, blank=True, null=True)
    Branch = models.CharField(max_length=40, blank=True, null=True)
    Address = models.CharField(max_length=100, blank=True, null=True)
    City = models.CharField(max_length=30, blank=True, null=True)
    State = models.CharField(max_length=30, blank=True, null=True)
    Zip = models.CharField(max_length=20, blank=True, null=True)
    Country = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) :
        return '{0}'.format(self.GST_No)



"""Vendor Staff Detail"""
class VendorStaffDetail(models.Model):
    Position = models.CharField(max_length=50, blank=True, null=True)
    Name = models.CharField(max_length=50, blank=True, null=True)
    Phone = models.CharField(max_length=50, blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    Photo = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)
    Address = models.TextField(blank=True, null=True)
    City = models.CharField(max_length=50, blank=True, null=True)
    State = models.CharField(max_length=50, blank=True, null=True)
    Country = models.CharField(max_length=50, blank=True, null=True)
    Zip = models.TextField(blank=True, null=True)
    Published = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return '{0}'.format(self.Position)


""" Vendor Sub Location """
class Sub_Location(models.Model):
    Location = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Location)


""" Vendor Material To """
class Material_To(models.Model):
    District = models.CharField(max_length=50, blank=True, null=True)
    SubLocation = models.ManyToManyField(Sub_Location, blank=True)

    def __str__(self) :
        return str(self.District)
    
    def natural_key(self):
        return self.SubLocation.Location


""" Vendor Material From """
class Material_From(models.Model):
    Type = models.CharField(max_length=300, blank=True, null=True)
    Name = models.CharField(max_length=50, blank=True, null=True)
    # Email = models.CharField(max_length=30, blank=True, null=True)
    # Phone = models.CharField(max_length=20, blank=True, null=True)
    Location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) :
        return str(self.Type)


""" Vendor Material Quality """
class MaterialQuality(models.Model):
    Quality = models.CharField(max_length=30, blank=True, null=True)
    Price = models.CharField(max_length=10, blank=True, null=True)


""" Vendor Material Supplying """
class Material_Supplying(models.Model):
    Material_From = models.ManyToManyField(Material_From, blank=True)
    Material_To = models.ManyToManyField(Material_To, blank=True)
    Material_Name = models.CharField(max_length=50, blank=True, null=True)
    Material_GST = models.CharField(max_length=20, blank=True, null=True)
    HSNCode = models.CharField(max_length=20, blank=True, null=True)
    Material_Type = models.CharField(max_length=1, choices=MATERIAL_CHOICES, default=1, blank=True, null=True)
    Quality = models.ManyToManyField(MaterialQuality, blank=True)
     
    def natural_key(self):
        data = {
            'Material_Name' : self.Material_Name,
            'Material_GST' : self.Material_GST,
            'HSNCode' : self.HSNCode,
            'Material_Type' : self.Material_Type,
        }
        MaterialQualityall = []
        MaterialFromall = []
        MaterialToall = []

        for j in self.Quality.all():
            MaterialQuality = {
                'Quality' : j.Quality,
                'Price' : j.Price,
            }
            MaterialQualityall.append(MaterialQuality)

        for j in self.Material_From.all():
            MaterialFrom = {
                'Type' : j.Type,
                'Location' : j.Location,
            }
            MaterialFromall.append(MaterialFrom)

        for j in self.Material_To.all():
            sublocationall = []
            MaterialTo = {
                'District' : j.District,
                'Sublocation' : sublocationall
            }
            for k in j.SubLocation.all():
                sublocationall.append(k.Location)
            MaterialToall.append(MaterialTo)
            
        data['MaterialQuality'] = MaterialQualityall
        data['MaterialFrom'] = MaterialFromall
        data['MaterialTo'] = MaterialToall
        
        return data

""" Venor models"""
class Vendor(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Agency = models.ManyToManyField(Agency, blank=True)
    Vendor_Type = models.CharField(max_length=1, choices=GST_TYPE_CHOICES, default=1, blank=True, null=True)
    Vendor_Name = models.CharField(max_length=100, blank=True, null=True)
    Company_Name = models.CharField(max_length=100, blank=True, null=True)
    Phone = models.CharField(max_length=100, blank=True, null=True)
    Email = models.CharField(max_length=100, blank=True, null=True)
    Photo = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)
    Address = models.CharField(max_length=100, blank=True, null=True)
    City = models.CharField(max_length=100, blank=True, null=True)
    State = models.CharField(max_length=100, blank=True, null=True)
    Zip = models.CharField(max_length=100, blank=True, null=True)
    Country = models.CharField(max_length=100, blank=True, null=True)
    GST_No = models.ManyToManyField(VendorGST, blank=True)
    TIN_No = models.ManyToManyField(VendorTIN, blank=True)
    PAN_No = models.ManyToManyField(VendorPAN, blank=True)
    Certificate = models.ManyToManyField(VendorCertificate, blank=True)
    # Material_From = models.ManyToManyField(Material_From, blank=True)
    # Material_To = models.ManyToManyField(Material_To, blank=True)
    Vendor_Category = models.CharField(max_length=300, blank=True, null=True)
    No_Of_Trucks = models.CharField(max_length=100, blank=True, null=True)
    Material_Supplying = models.ManyToManyField(Material_Supplying, blank=True)
    Payment_Capabilities = models.CharField(max_length=100, blank=True, null=True)
    Vendor_Staff_Detail = models.ManyToManyField(VendorStaffDetail, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.Vendor_Name)

    def natural_key(self):
        return self.Vendor_Name