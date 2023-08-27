from django.contrib import admin
from apps.customers import models
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['Founder_Name', 'Company_Name', 'Founder_Email', 'GST_Type']

admin.site.register(models.Customer, CustomerAdmin)


class CustomerStaffAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Contact_No', 'Email', 'Position', 'Location']

admin.site.register(models.CustomerStaff, CustomerStaffAdmin)


class CustomerDeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ['Branch']

admin.site.register(models.CustomerDeliveryAddress, CustomerDeliveryAddressAdmin)



class CustomerBranchAdmin(admin.ModelAdmin):
    list_display = ['Payment_Term']

admin.site.register(models.Branch, CustomerBranchAdmin)



class CustomerBankAccountAdmin(admin.ModelAdmin):
    list_display = ['Account_Holder_Name', 'Account_Category', 'Account_No', 'IFSC_Code', 'Branch', 'Register_Phone']

admin.site.register(models.CustomerBankAccounts, CustomerBankAccountAdmin)


class CustomerGSTBillingAddressAdmin(admin.ModelAdmin):
    list_display = ['GST_No', 'Scan_Copy', 'Address', 'Mobile', 'Mail_Id']

admin.site.register(models.CustomerGSTBillingAddress, CustomerGSTBillingAddressAdmin)

admin.site.register(models.CustomerPhoneNumber)