from django.contrib import admin
from apps.purchase.models import PurchaseMaterialEntry, PurchaseRemainder, purchaseInvoice,PurchaseNetAmount, SinglePurchaseEntry, PurchaseEntry
# Register your models here.

admin.site.register(PurchaseMaterialEntry)
admin.site.register(PurchaseRemainder)
admin.site.register(PurchaseNetAmount)
admin.site.register(purchaseInvoice)
admin.site.register(SinglePurchaseEntry)
admin.site.register(PurchaseEntry)