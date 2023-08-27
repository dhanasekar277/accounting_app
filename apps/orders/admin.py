from django.contrib import admin
from apps.orders.models import MaterialOrder, Order, PONumber, POMaterialInfo
# Register your models here.
 

class MaterialOrderAdmin(admin.ModelAdmin):
    list_display = ['Vendor', 'Material_Name', 'Load', 'Expected_Date', 'Quantity']

admin.site.register(MaterialOrder, MaterialOrderAdmin)


# class POMaterialInfoAdmin(admin.ModelAdmin):
#     list_display = [ 'PO_Quantity', 'PO_Rates',  'PO_Terms', 'Published']

# admin.site.register(POMaterialInfo, POMaterialInfoAdmin)


# class PONumberAdmin(admin.ModelAdmin):
#     list_display = ['PO_Type', 'PO_Number', 'PO_Recived_Name', 'PO_Recived_Mail', 'PO_Date']

# admin.site.register(PONumber, PONumberAdmin)
admin.site.register(POMaterialInfo)
admin.site.register(PONumber)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['Agency', 'Sales_Company', 'PO_Number']

admin.site.register(Order, OrderAdmin)