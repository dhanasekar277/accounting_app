from django.contrib import admin
from apps.voucher.models import PurchaseInfo, VourchersAmount, VoucherDetail, VoucherSignature, Voucher,VoucherVendorInfo
# Register your models here.

admin.site.register(PurchaseInfo)
admin.site.register(VoucherSignature)
admin.site.register(VourchersAmount)
admin.site.register(VoucherDetail)
admin.site.register(Voucher)
admin.site.register(VoucherVendorInfo)
