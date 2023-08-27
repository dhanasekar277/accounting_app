from django.contrib import admin
from . models import purchase_entry,sales_entry,purchase_material,sales_material,CashUser
# Register your models here.
admin.site.register(purchase_entry)
admin.site.register(sales_entry)
admin.site.register(purchase_material)
admin.site.register(sales_material)
admin.site.register(CashUser)
