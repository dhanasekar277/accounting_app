from django.contrib import admin
from apps.quotations.models import PurchaseQuotation, SalesQuotation, Quotation, CustomerQuotationDetail, CustomerQuotationTerms, VendorQuotationDetail

# Register your models here.
admin.site.register(CustomerQuotationDetail)
admin.site.register(CustomerQuotationTerms)
admin.site.register(VendorQuotationDetail)
admin.site.register(PurchaseQuotation)
admin.site.register(SalesQuotation)
admin.site.register(Quotation)