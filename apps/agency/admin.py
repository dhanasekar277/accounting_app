from statistics import mode
from django.contrib import admin
from apps.agency import models
# Register your models here.


"""Agency table"""
class AgencyAdmin(admin.ModelAdmin):
    list_display = ['Name', 'User', 'Email', 'GST_Number', 'PAN_Number', 'Timestamp']

admin.site.register(models.Agency, AgencyAdmin)

admin.site.register(models.AgencyPhone)


"""Aggency Certificated"""
class AgencyCerticficateAdmin(admin.ModelAdmin):
    list_display = ['Certificate_Name', 'Certificate_Scan_Copy', 'Timestamp']

admin.site.register(models.AgencyCertificate, AgencyCerticficateAdmin)


"""Aggency Acc No"""
class AgencyBankAccountAdmin(admin.ModelAdmin):
    list_display = ['Account_Number', 'IFSC_Code', 'Branch', 'Register_Email', 'Register_Phone', 'Timestamp']

admin.site.register(models.AgencyBankAccount, AgencyBankAccountAdmin)
admin.site.register(models.Signature)