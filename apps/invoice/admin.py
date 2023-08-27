from django.contrib import admin
from apps.invoice.models import SalesInvoice, SingleSalesInvoice, DCDetail
# Register your models here.
admin.site.register(DCDetail)
admin.site.register(SingleSalesInvoice)
admin.site.register(SalesInvoice)
