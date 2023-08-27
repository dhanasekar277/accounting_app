from django.http import HttpResponse
from django.shortcuts import render
from apps.purchase.models import PurchaseEntry
from apps.agency.models import Agency
from apps.voucher.models import VoucherDetail, Voucher
from apps.invoice.models import SalesInvoice
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from django.core.serializers.json import Serializer
from apps.balancesheet.views import CustomSerializer

# NET PURCHASE
def NetPurchase(request):
    # Search And PAgination
    active_agency = Agency.objects.all().filter(Active=True).first()
    if request.GET.get("calander_from"):
        fromdate = request.GET.get("calander_from")
        todate = request.GET.get("calander_to")
        if active_agency is not None:
            voucherdetails = Voucher.objects.filter(Date__range=[fromdate, todate],quotation__agency=active_agency.id).order_by("-id")
    elif request.GET.get("search"):
        query = request.GET.get("search")
        lookups = Q(voucher__vendorDetail__Name__icontains=query)
        if active_agency is not None:
            voucherdetails = Voucher.objects.filter(lookups, quotation__agency=active_agency.id).order_by("-id")
    else:
        voucherdetails = Voucher.objects.filter(quotation__agency=active_agency).order_by("-id")

    # Total Net
    totalwgst = voucherdetails.aggregate(Sum("voucher__amount__total_amount"))
    totalwogst = voucherdetails.aggregate(Sum("voucher__amount__total"))
    sgstamount = voucherdetails.aggregate(Sum("voucher__amount__sgst_amount"))
    cgstamount = voucherdetails.aggregate(Sum("voucher__amount__cgst_amount"))
    totalnetpaid = voucherdetails.aggregate(
        Sum("purchase__entries__netAmount__AmountPayyed")
    )
    totalnetbalance = voucherdetails.aggregate(
        Sum("purchase__entries__netAmount__Balance")
    )

    paginator = Paginator(voucherdetails, 10)
    voucherdetails = paginator.page(request.GET.get("page", 1))

    return render(
        request,
        "net_details/netpurchase.html",
        {
            "voucherdetails": voucherdetails,
            "totalwgst": totalwgst,
            "totalwogst": totalwogst,
            "sgstamount": sgstamount,
            "cgstamount": cgstamount,
            "totalnetpaid": totalnetpaid,
            "totalnetbalance": totalnetbalance,
        },
    )


# NET PAYABLE
def NetPaymentPayable(request):
    active_agency = Agency.objects.all().filter(Active=True).first()
    # Search And PAgination
    if request.GET.get("calander_from"):
        fromdate = request.GET.get("calander_from")
        todate = request.GET.get("calander_to")
        if active_agency is not None:
            voucherdetails = Voucher.objects.filter(Date__range=[fromdate, todate],quotation__agency=active_agency.id).order_by("-id")
    elif request.GET.get("search"):
        query = request.GET.get("search")
        lookups = Q(voucher__vendorDetail__Name__icontains=query)
        if active_agency is not None:
            voucherdetails = Voucher.objects.filter(lookups, quotation__agency=active_agency.id).order_by("-id")
    else:
        voucherdetails = Voucher.objects.filter(quotation__agency=active_agency).order_by("-id")

    # Total Net PURCHASE
    totalwgst = voucherdetails.aggregate(Sum("voucher__amount__total_amount"))
    totalwogst = voucherdetails.aggregate(Sum("voucher__amount__total"))
    sgstamount = voucherdetails.aggregate(Sum("voucher__amount__sgst_amount"))
    cgstamount = voucherdetails.aggregate(Sum("voucher__amount__cgst_amount"))
    totalnetpaid = voucherdetails.aggregate(Sum("purchase__entries__netAmount__AmountPayyed"))
    totalnetbalance = voucherdetails.aggregate(Sum("purchase__entries__netAmount__Balance"))

    paginator = Paginator(voucherdetails, 10)
    voucherdetails = paginator.page(request.GET.get("page", 1))

    return render(
        request,
        "net_details/netpayable.html",
        {
            "voucherdetails": voucherdetails,
            "totalwgst": totalwgst,
            "totalwogst": totalwogst,
            "sgstamount": sgstamount,
            "cgstamount": cgstamount,
            "totalnetpaid": totalnetpaid,
            "totalnetbalance": totalnetbalance,
        },
    )


# NET SALES
def NetSales(request):
    # Search And PAgination
    active_agency = Agency.objects.all().filter(Active=True).first()
    if request.GET.get("calander_from"):
        fromdate = request.GET.get("calander_from")
        todate = request.GET.get("calander_to")
        if active_agency is not None:
            salesinvoices = SalesInvoice.objects.filter(Date__range=[fromdate, todate], saleid__orderid__Agency=active_agency.id).order_by("-id")
    elif request.GET.get("search"):
        query = request.GET.get("search")
        lookups = Q(saleid__sales__customer__customerid__Company_Name__icontains=query)
        if active_agency is not None:
            salesinvoices = SalesInvoice.objects.filter(lookups, saleid__orderid__Agency=active_agency.id).order_by("-id").distinct()
    else:
        salesinvoices = SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency).order_by("-id")

    # Total Net Sales Start
    totalwgst = salesinvoices.aggregate(
        Sum("saleid__sales__netAmount__WithGSTNetTotalAmount")
    )
    totalwogst = salesinvoices.aggregate(
        Sum("saleid__sales__netAmount__WithOutGSTNetTotalAmount")
    )
    totalnetamount = salesinvoices.aggregate(Sum("saleid__sales__netAmount__Balance"))

    paginator = Paginator(salesinvoices, 10)
    salesinvoices = paginator.page(request.GET.get("page", 1))

    return render(
        request,
        "net_details/netsales.html",
        {
            "salesinvoices": salesinvoices,
            "totalwgst": totalwgst,
            "totalwogst": totalwogst,
            "totalnetamount": totalnetamount,
            'gst' : SalesInvoice.objects.values_list('invoice__orderid__Materials__Product_Name__GST').order_by('-id')
        },
    )

# NET RECIVEABLE
def NetPaymentRecivable(request):
    # Search And Pagination
    active_agency = Agency.objects.all().filter(Active=True).first()
    if request.GET.get("calander_from"):
        fromdate = request.GET.get("calander_from")
        todate = request.GET.get("calander_to")
        if active_agency is not None:
            salesinvoices = SalesInvoice.objects.filter(Date__range=[fromdate, todate],saleid__orderid__Agency=active_agency.id).order_by("-id")
    elif request.GET.get("search"):
        query = request.GET.get("search")
        lookups = Q(saleid__sales__customer__customerid__Company_Name__icontains=query)
        if active_agency is not None:
            salesinvoices = SalesInvoice.objects.filter(lookups, saleid__orderid__Agency=active_agency.id).order_by("-id").distinct()
    else:
        salesinvoices = SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency).order_by("-id")

    # Total Net Sales Start
    totalwgst = salesinvoices.aggregate(
        Sum("saleid__sales__netAmount__WithGSTNetTotalAmount")
    )
    totalwogst = salesinvoices.aggregate(
        Sum("saleid__sales__netAmount__WithOutGSTNetTotalAmount")
    )
    recivedamount = salesinvoices.aggregate(
        Sum("saleid__sales__netAmount__AmountPayyed")
    )
    netreciveable = salesinvoices.aggregate(Sum("saleid__sales__netAmount__Balance"))
    # Total Net Sales END

    paginator = Paginator(salesinvoices, 10)
    salesinvoices = paginator.page(request.GET.get("page", 1))

    return render(
        request,
        "net_details/netreciveable.html",
        {
            "salesinvoices": salesinvoices,
            "totalwgst": totalwgst,
            "totalwogst": totalwogst,
            "recivedamount": recivedamount,
            "netreciveable": netreciveable,
        },
    )


def NetPurchaseJson(request):
    custom_serializers = CustomSerializer()
    queryset = VoucherDetail.objects.all()
    # total = VoucherDetail.objects.all().aggregate(Sum('amount__total_amount'))
    particular_purchase = custom_serializers.serialize(queryset,
    use_natural_foreign_keys=True, 
    fields=('Date',
        'amount',
        'vendorDetail__GSTNo__Trade_Name',
        'vendorDetail__GSTNo__Leggal_Name',
        'vendorDetail__GSTNo__GST_No',
        'quotation'
        ))
    return HttpResponse(particular_purchase)


def NetSalesJson(request):
    custom_serializers = CustomSerializer()
    queryset = SalesInvoice.objects.all()
    particular_sales = custom_serializers.serialize(queryset,
    use_natural_foreign_keys=True, 
    fields=('Date',
        'saleid',
        'invoice',
        'saleid__orderid__Sales_Company__Company_Name',
        )
        )
    return HttpResponse(particular_sales)


