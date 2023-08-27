from unicodedata import name
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

""" Agency Certificate """
class AgencyCertificate(models.Model):
    Certificate_Name = models.CharField(max_length=100, blank=True, null=True)
    Certificate_Scan_Copy = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)
    Timestamp = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return str(self.Certificate_Name)


""" Agency bank account """
class AgencyBankAccount(models.Model):
    Account_Holder_Name = models.CharField(max_length=100, blank=True, null=True)
    Account_Holder_Position = models.CharField(max_length=100, blank=True, null=True)
    Account_Number = models.CharField(max_length=100, blank=True, null=True)
    IFSC_Code = models.CharField(max_length=100, blank=True, null=True)
    Branch = models.CharField(max_length=100, blank=True, null=True)
    Bank_Name = models.CharField(max_length=100, blank=True, null=True)
    Register_Email = models.CharField(max_length=100, blank=True, null=True)
    Register_Phone = models.CharField(max_length=100, blank=True, null=True)
    Timestamp = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Branch)


""" Agency Phone """
class AgencyPhone(models.Model):
    ph_name=models.CharField(max_length=200, blank=True, null=True)
    Phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) :
        return str(self.Phone)

""" Agency """
class Agency(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100, blank=True, null=True)
    Email = models.CharField(max_length=100, blank=True, null=True)
    Phone = models.ManyToManyField(AgencyPhone, blank=True)
    Logo = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)
    Bank_Account = models.ManyToManyField(AgencyBankAccount, blank=True)
    Active = models.BooleanField(default=False)
    Timestamp = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    GST_Number = models.CharField(max_length=100, blank=True, null=True)
    PAN_Number = models.CharField(max_length=100, blank=True, null=True)
    Certificates = models.ManyToManyField(AgencyCertificate, blank=True)
    Address = models.CharField(max_length=100, blank=True, null=True)
    City = models.CharField(max_length=100, blank=True, null=True)
    Zip = models.CharField(max_length=100, blank=True, null=True)
    State = models.CharField(max_length=100, blank=True, null=True)
    Country = models.CharField(max_length=100, blank=True, null=True)
    Location_Url = models.CharField(max_length=100, blank=True, null=True)
    Tin = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateField(auto_now=True, null=True)
    
    class Meta:
        ordering = ['-Timestamp']

    def __str__(self) :
        return str(self.Name)

class Signature(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    signature = models.ImageField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self) :
        return str(self.name)
