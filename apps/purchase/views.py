from cgitb import lookup
from pickle import TRUE
from tkinter import FLAT
from django.shortcuts import render
from apps.orders.models import Order
from apps.agency.models import Agency
from apps.voucher.models import Voucher
from apps.purchase.models import PurchaseEntry, SinglePurchaseEntry, PurchaseMaterialEntry
from apps.quotations.models import Quotation
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.


def Purchases(request):
    active_agency = Agency.objects.all().filter(Active=True).first()
    if(request.GET.get('search')):
        query = request.GET.get('search')
        lookups = Q(quotation__sales__customer__Company_Name__icontains=query) | Q(quotation__sales__customer__Founder_Name__icontains=query)
        if active_agency is not None:
            purchase = PurchaseEntry.objects.filter(lookups,quotation__agency=active_agency.id).order_by('-id')
    else:
        purchase = PurchaseEntry.objects.filter(quotation__agency=active_agency).order_by('-id')
    
    paginator = Paginator(purchase, 10)
    purchase = paginator.page(request.GET.get('page', 1))
    voucherNo = Voucher.objects.filter(voucher__amount__Info__VoucherNo__isnull= False).values("purchase__quotation__order__id", "voucher__amount__Info__VoucherNo")
    print(voucherNo)
    context = {
        'purchase': purchase,
        "autoVoucherNo" : voucherNo
    }
    return render(request, 'purchase/purchase.html', context)


def PurchaseView(request, quotation, vendor):
    mat_id = request.GET['mat-id']
    if mat_id : 
        context = {
            'quotations': Quotation.objects.filter(id=quotation),
            'mat_id': mat_id
        }
    else :
        context = {
            'purchase': PurchaseEntry.objects.filter(quotation=quotation, vendorId=vendor),
        }
    return render(request, 'purchase/purchase-view.html', context)



def PurchasesEntries(request, id):
    entries = SinglePurchaseEntry.objects.filter(id=id)
    context = {
        'entries': entries
    }
    return render(request, 'purchase/purchase-entries.html', context)


def PurchasesInvoice(request, quotation, vendor):
    entries = PurchaseEntry.objects.filter(quotation=quotation, vendorId=vendor).order_by('-id')
    context = {
        'entries': entries
    }
    return render(request, 'purchase/purchase-invoice.html', context)




def PurchasesVoucher(request):
    return render(request, 'voucher/purchase-voucher.html')

def PurchasesVoucherAdd(request):
    active_agency = Agency.objects.all().filter(Active=True)
    context= {
        'order_obj' : Order.objects.all().filter(Agency=active_agency[0].id, Approved = True),
    }
    return render(request, 'voucher/purchase-voucher-add.html', {'context': context})
 
def AddPurchase(request):
    active_agency = Agency.objects.all().filter(Active=True)
    context= {
        'order_obj' : Order.objects.all().filter(Agency=active_agency[0].id, Approved = True),
    }
    return render(request, 'purchase/purchase-add.html', {'context': context})



def GetPurchaseMaterial(request, pk):
    particular_expence = serializers.serialize('json', PurchaseMaterialEntry.objects.filter(p_id=pk).order_by('-id'))
    return HttpResponse(particular_expence)


