from django.shortcuts import render, HttpResponse
from .models import BankEntry
from django.core.paginator import Paginator
from apps.agency.models import Agency
from django.db.models import Q, Sum
from django.core import serializers
from apps.voucher.models import VoucherDetail, Voucher
from apps.invoice.models import SalesInvoice
from apps.customers.models import Customer
from apps.vendors.models import Vendor
from itertools import chain

# Create your views here.


# def BankEntries(request):
#     # Search And PAgination
#     if request.GET.get('calander_from'):
#         fromdate = request.GET.get('calander_from')
#         todate = request.GET.get('calander_to')
#         entries = BankEntry.objects.filter(Date__range=[fromdate,todate]).order_by('-id')
#     elif(request.GET.get('search')):
#         query = request.GET.get('search')
#         entries = BankEntry.objects.filter(Q(Cheque_No__icontains=query) | Q(Expence_Type__icontains=query) | Q(Name__icontains=query)).order_by('-id')
#     else:
#         entries = BankEntry.objects.all().order_by('-id')

#     paginator = Paginator(entries, 10)
#     entries = paginator.page(request.GET.get('page', 1))

#     return render(request, 'bank-entries/bankentries.html', {
#         'entries' : entries,
#         'customer_names' : Customer.objects.only('Company_Name'),
#         'vendor_names' : Vendor.objects.only('Company_Name')
#     })


def BankEntries(request):
    # Search And PAgination
    active_agency = Agency.objects.all().filter(Active=True).first()
    if request.GET.get("calander_from"):
        fromdate = request.GET.get("calander_from")
        todate = request.GET.get("calander_to")
        if active_agency is not None:
            voucherdetails = Voucher.objects.filter(
                Date__range=[fromdate, todate], quotation__agency=active_agency.id
            ).order_by("-id")
            salesinvoices = SalesInvoice.objects.filter(
                Date__range=[fromdate, todate], saleid__orderid__Agency=active_agency.id
            ).order_by("-id")
    elif request.GET.get("search"):
        query = request.GET.get("search")
        if active_agency is not None:
            voucherlookups = Q(voucher__vendorDetail__Name__icontains=query)
            voucherdetails = Voucher.objects.filter(
                voucherlookups, quotation__agency=active_agency.id
            ).order_by("-id")
            saleslookups = Q(
                saleid__sales__customer__customerid__Company_Name__icontains=query
            )
            salesinvoices = SalesInvoice.objects.filter(
                saleslookups, saleid__orderid__Agency=active_agency.id
            ).order_by("-id")
    else:
        voucherdetails = Voucher.objects.filter(
            quotation__agency=active_agency
        ).order_by("-id")
        salesinvoices = SalesInvoice.objects.filter(
            saleid__orderid__Agency=active_agency
        ).order_by("-id")

    # Total voucher Net
    voutotalwgst = voucherdetails.aggregate(Sum("voucher__amount__total_amount"))
    voutotalwogst = voucherdetails.aggregate(Sum("voucher__amount__total"))
    sgstamount = voucherdetails.aggregate(Sum("voucher__amount__sgst_amount"))
    cgstamount = voucherdetails.aggregate(Sum("voucher__amount__cgst_amount"))
    totalnetpaid = voucherdetails.aggregate(
        Sum("purchase__entries__netAmount__AmountPayyed")
    )
    totalnetbalance = voucherdetails.aggregate(
        Sum("purchase__entries__netAmount__Balance")
    )
    totalgstpaid = voucherdetails.aggregate(
        Sum("purchase__entries__netAmount__GstPayyed")
    )
    totalgstbalance = voucherdetails.aggregate(
        Sum("purchase__entries__netAmount__GstBalance")
    )

    paginator = Paginator(voucherdetails, 10)
    voucherdetails = paginator.page(request.GET.get("page", 1))

    # Total Sales Net
    totalwgst = salesinvoices.aggregate(
        Sum("saleid__sales__netAmount__WithGSTNetTotalAmount")
    )
    totalwogst = salesinvoices.aggregate(
        Sum("saleid__sales__netAmount__WithOutGSTNetTotalAmount")
    )
    totalnetamountpaid = salesinvoices.aggregate(Sum("saleid__sales__netAmount__AmountPayyed"))
    totalnetamount = salesinvoices.aggregate(Sum("saleid__sales__netAmount__Balance"))
    totalgstamount = salesinvoices.aggregate(Sum("saleid__sales__netAmount__GstTotal"))
    totalgstamountpaid = salesinvoices.aggregate(Sum("saleid__sales__netAmount__GstBalance"))

    paginator = Paginator(salesinvoices, 10)
    salesinvoices = paginator.page(request.GET.get("page", 1))

    return render(
        request,
        "bank-entries/bankentries.html",
        {
            "active_agency": active_agency,
            "voucherdetails": voucherdetails,
            "voutotalwgst": voutotalwgst,
            "voutotalwogst": voutotalwogst,
            "sgstamount": sgstamount,
            "cgstamount": cgstamount,
            "totalnetpaid": totalnetpaid,
            "totalgstpaid": totalgstpaid,
            "totalgstbalance": totalgstbalance,
            "totalnetbalance": totalnetbalance,
            "salesinvoices": salesinvoices,
            "totalwgst": totalwgst,
            "totalwogst": totalwogst,
            "totalnetamount": totalnetamount,
            "totalnetamountpaid": totalnetamountpaid,
            "totalgstamount": totalgstamount,
            "totalgstamountpaid": totalgstamountpaid,
            "gst": SalesInvoice.objects.values_list(
                "invoice__orderid__Materials__Product_Name__GST"
            ).order_by("-id"),
        },
    )


def bankentryView(request, id, type):
    if type == 'vendor':
        queryset = BankEntry.objects.filter(vendorId=id).order_by("-id")
    elif type == 'customer':
        queryset = BankEntry.objects.filter(vendorId=id).order_by("-id")
    bankval = serializers.serialize(
        "json", queryset
    )
    return HttpResponse(bankval)
