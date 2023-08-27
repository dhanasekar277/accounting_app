from django.shortcuts import render
from apps.orders.models import Order
from apps.purchase.models import PurchaseEntry
from apps.voucher.models import VoucherDetail
from django.http import HttpResponse, JsonResponse
from apps.purchase.models import PurchaseEntry
from apps.voucher.models import Voucher
# Create your views here.

# def PurchasesVoucher(request):
#     return render(request, 'voucher/purchase-voucher.html')

def VoucherView(request, quotation, vendorId):
    voucher = VoucherDetail.objects.filter(quotation=quotation, VendorId=vendorId)
    purchase = PurchaseEntry.objects.filter(quotation=quotation, vendorId=vendorId)

    context = {
        'quotation_id' : quotation,
        'quotation': PurchaseEntry.objects.filter(quotation=quotation),
        'voucher': voucher,
        'voucher_count': voucher.count(),
        'purchaseId': purchase[0]
    }
    
    return render(request, 'voucher/voucher-view.html', context)


def GetVoucherCount(request, id):
    voucher = VoucherDetail.objects.filter(VendorId=id).count()
    voucher_total = VoucherDetail.objects.all().count()
    context = {
        'count': voucher,
        'total_voucher':voucher_total
    }
    return JsonResponse(context)

def VoucherView(request, quotation, vendorId):
    voucher = VoucherDetail.objects.filter(quotation=quotation, VendorId=vendorId)
    all_voucher = Voucher.objects.filter(quotation=quotation).first()
    purchase = PurchaseEntry.objects.filter(quotation=quotation, vendorId=vendorId).first()

    context = {
        'quotation_id' : quotation,
        'quotation': PurchaseEntry.objects.filter(quotation=quotation),
        'voucher': voucher,
        'all_voucher':all_voucher,
        'voucher_count': voucher.count(),
        'purchaseId': purchase
    }
    
    return render(request, 'voucher/voucher-view.html', context)