from django.contrib import admin
from apps.vendors import models

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ['Vendor_Type', 'Vendor_Name', 'Company_Name', 'Phone', 'Email', 'No_Of_Trucks']

admin.site.register(models.Vendor, VendorAdmin)


# Register your models here.
class VendorStaffDetailAdmin(admin.ModelAdmin):
    list_display = ['Position', 'Name', 'Phone', 'Email', 'Country']

admin.site.register(models.VendorStaffDetail, VendorStaffDetailAdmin)

 
# Register your models here.
class VendorGSTBankAccountAdmin(admin.ModelAdmin):
    list_display = ['Address', 'City', 'State', 'Zip']

admin.site.register(models.VendorGSTBankAccount, VendorGSTBankAccountAdmin)


# # Register your models here.
class VendorCertificateAdmin(admin.ModelAdmin):
    list_display = ['Vendor_Certificate_Name', 'Vendor_Certificate_Scan_Copy']

admin.site.register(models.VendorCertificate, VendorCertificateAdmin)

admin.site.register(models.VendorTIN)
admin.site.register(models.VendorPAN)
admin.site.register(models.Material_To)
admin.site.register(models.Material_From)

class MaterialQualityAdmin(admin.ModelAdmin):
    list_display = ['Quality', 'Price']

admin.site.register(models.MaterialQuality, MaterialQualityAdmin)

# admin.site.register(models.MaterialQuality)
admin.site.register(models. Material_Supplying)
admin.site.register(models.Sub_Location)
class VendorGSTAdmin(admin.ModelAdmin):
    list_display = ['Leggal_Name', 'Trade_Name', 'Holder_Name', 'GST_No', 'Phone', 'Name', 'Email']

admin.site.register(models.VendorGST, VendorGSTAdmin)
