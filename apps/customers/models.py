from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

CATEGORY_CHOICES =(
    ("0", "Personal"),
    ("1", "Registered Account"),
)


""" Customer bank account models"""
class CustomerBankAccounts(models.Model):
    Account_Holder_Name = models.CharField(max_length=100, null=True, blank=True)
    Account_Category = models.CharField(max_length=1, default=0, choices=CATEGORY_CHOICES, null=True, blank=True)
    Account_No = models.CharField(max_length=100, null=True, blank=True)
    Account_Position = models.CharField(max_length=100, null=True, blank=True)
    IFSC_Code = models.CharField(max_length=100, null=True, blank=True)
    Branch = models.CharField(max_length=100, null=True, blank=True)
    Register_Phone = models.CharField(max_length=100, null=True, blank=True)
    Register_Email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.Account_Holder_Name, self.Branch)


""" Customer GST Billing Address """
class CustomerGSTBillingAddress(models.Model):
    Leggal_Name = models.CharField(max_length=100, null=True, blank=True)
    Trade_Name = models.CharField(max_length=100, null=True, blank=True)
    GST_No = models.CharField(max_length=100, null=True, blank=True)
    Scan_Copy = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)
    Address = models.TextField(null=True, blank=True)
    City = models.CharField(max_length=20, null=True, blank=True)
    State = models.CharField(max_length=30, null=True, blank=True)
    Zip = models.CharField(max_length=10, null=True, blank=True)
    Country = models.CharField(max_length=30, null=True, blank=True)
    Location_Url = models.URLField(max_length=100, null=True, blank=True)
    Mobile = models.CharField(max_length=20, null=True, blank=True)
    Mail_Id = models.CharField(max_length=50, null=True, blank=True)
    Account_No = models.CharField(max_length=100, null=True, blank=True)
    GST_Bank = models.CharField(max_length=50, null=True, blank=True)
    GST_Branch = models.CharField(max_length=50, null=True, blank=True)
    IFSC = models.CharField(max_length=50, null=True, blank=True)
    Holder_Name = models.CharField(max_length=50, null=True, blank=True)
    Position = models.CharField(max_length=50, null=True, blank=True)
    Photo = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.GST_No, self.City)


""" Delivery Address Models """
class CustomerDeliveryAddress(models.Model):
    Customer_Name = models.CharField(max_length=200, null=True, blank=True)
    Branch = models.CharField(max_length=200, null=True, blank=True)
    URL_Location_Of_The_Unloading_Place = models.CharField(max_length=200, null=True, blank=True)
    URL_Office_Location  = models.CharField(max_length=200, null=True, blank=True)
    URL_Of_Owner_House  = models.CharField(max_length=200, null=True, blank=True)
    Invoice_Submitting_URL = models.CharField(max_length=200, null=True, blank=True)
    Payment_Collecting_URL = models.CharField(max_length=200, null=True, blank=True)
    Add_other_URL = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.Customer_Name, self.Branch)

GST_TYPE = (
    ("0", "GST Registered"),
    ("1", "Unregistered")
)
 
""" Customer Address """
class CustomerStaff(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True) 
    Contact_No = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(max_length=30, null=True, blank=True)
    Position = models.CharField(max_length=100) 
    Location = models.TextField(null=True, blank=True) 
    City = models.CharField(max_length=50, null=True, blank=True)
    Zip = models.CharField(max_length=50, null=True, blank=True)
    State = models.CharField(max_length=50, null=True, blank=True) 
    Country = models.CharField(max_length=50, null=True, blank=True)
    Photo = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.Name, self.Position)


""" Branch delivery address """
class BranchDeliveryAddres(models.Model):
    Address = models.TextField(null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    Zip = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    NickName = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.Address, self.NickName)



""" Branches details """
class Branch(models.Model):
    Billing_Address = models.ForeignKey(CustomerGSTBillingAddress, on_delete=models.CASCADE, null=True, blank=True)
    Delivery_Address = models.ManyToManyField(BranchDeliveryAddres, blank=True)
    Staff_Detail = models.ManyToManyField(CustomerStaff, blank=True)
    Payment_Term = models.CharField(max_length=100, null=True, blank=True)
    


""" PAN No details """
class PANNo(models.Model):
    PAN_No = models.CharField(max_length=100, null=True, blank=True)
    PAN_Scan_Copy = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return str(self.PAN_No)


""" Certificate details """
class CustomerCertifcate(models.Model):
    Certificate_Name = models.CharField(max_length=100, null=True, blank=True)
    Scan_Copy = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return str(self.Certificate_Name)


""" Certificate details """
class TINNo(models.Model):
    TIN_No = models.CharField(max_length=100, null=True, blank=True)
    Scan_Copy = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return str(self.TIN_No)


"""Customer Founder PhoneNumber Details"""
class CustomerPhoneNumber(models.Model):
    customer_name= models.CharField(max_length=50, null=True, blank=True)
    Phone_Number = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.Phone_Number)

 
"""delivery address for sales company should be only one"""
class Customer(models.Model):
    # map customer name
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Company_Name = models.CharField(max_length=100, null=True, blank=True)
    Company_Address = models.TextField(null=True, blank=True)
    Company_Email = models.EmailField(max_length=100, null=True, blank=True)
    Company_Logo = models.FileField(upload_to ='uploads/%Y/%m/%d/', blank=True, null=True)
    Company_City = models.CharField(max_length=100, null=True, blank=True)
    Company_State = models.CharField(max_length=100, null=True, blank=True)
    Company_Zip = models.CharField(max_length=100, null=True, blank=True)
    Company_Country = models.CharField(max_length=100, null=True, blank=True)
    Founder_Name = models.CharField(max_length=100, null=True, blank=True)
    Founder_Phone = models.ManyToManyField(CustomerPhoneNumber, blank=True)
    Founder_Email = models.CharField(max_length=50, null=True, blank=True)
    Founder_Address = models.TextField(null=True, blank=True)
    Founder_City = models.CharField(max_length=100, null=True, blank=True)
    Founder_State = models.CharField(max_length=100, null=True, blank=True)
    Founder_Zip = models.CharField(max_length=100, null=True, blank=True)
    Founder_Country = models.CharField(max_length=100, null=True, blank=True)
    delivery_Address = models.TextField(null=True, blank=True)
    delivery_City = models.CharField(max_length=100, null=True, blank=True)
    delivery_State = models.CharField(max_length=100, null=True, blank=True)
    delivery_Zip = models.CharField(max_length=100, null=True, blank=True)
    delivery_Country = models.CharField(max_length=100, null=True, blank=True)
    Customer_Staff_Account = models.ManyToManyField(CustomerStaff, blank=True)
    Bank_Account = models.ManyToManyField(CustomerBankAccounts, blank=True)
    Branches = models.ManyToManyField(Branch, blank=True)
    # Delivery_Address = models.ManyToManyField(CustomerDeliveryAddress, blank=True)
    GST_Type = models.CharField(max_length=1, choices=GST_TYPE, blank=True)
    TIN_No = models.ManyToManyField(TINNo, blank=True)
    GST_No = models.ManyToManyField(CustomerGSTBillingAddress, blank=True)
    PAN_No = models.ManyToManyField(PANNo, blank=True)
    Certificate = models.ManyToManyField(CustomerCertifcate, blank=True)
    No_Of_Project = models.CharField(max_length=10, null=True, blank=True)
    Remarks = models.TextField(null=True, blank=True)
    Payment_Terms = models.CharField(max_length=100, null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.Founder_Name)
