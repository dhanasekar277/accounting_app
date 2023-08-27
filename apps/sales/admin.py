from django.contrib import admin
from apps.sales.models import Total, CustomerInfo, SalesMaterialInfo, Sales,SalesCollection
# Register your models here.

admin.site.register(Total)
admin.site.register(CustomerInfo)
admin.site.register(SalesMaterialInfo)
admin.site.register(Sales)
admin.site.register(SalesCollection)
