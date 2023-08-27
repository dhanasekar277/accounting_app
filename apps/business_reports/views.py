from django.shortcuts import render
from apps.agency.models import Agency
from apps.invoice.models import SalesInvoice
from apps.sales.models import Sales
from apps.purchase.models import SinglePurchaseEntry
from apps.customers.models import Customer
from apps.vendors.models import Vendor
from django.core.paginator import Paginator
from django.db.models import Q, Sum


# Create your views here.

def customerSalesReports(request, pk=None):
    # Search And Pagination
    active_agency = Agency.objects.all().filter(Active=True).first()
    if request.GET.get("calander_from"):
        fromdate = request.GET.get("calander_from")
        todate = request.GET.get("calander_to")
        if active_agency is not None:
            sales = Sales.objects.filter(doc__range=[fromdate, todate],orderid__Agency=active_agency.id,customer__customerid = pk).order_by("-id")
    elif request.GET.get("search"):
        query = request.GET.get("search")
        lookups = Q(customer__customerid__Company_Name__icontains=query) | Q(customer__customerid__Founder_Name__icontains=query)
        if active_agency is not None:
            sales = Sales.objects.filter(lookups, orderid__Agency=active_agency.id).order_by("-id").distinct()
    else:
        sales = Sales.objects.filter(orderid__Agency=active_agency,customer__customerid = pk).order_by("-id")
        
    paginator = Paginator(sales, 10)
    sales = paginator.page(request.GET.get("page", 1))
    customers = Customer.objects.all().values('id', 'Company_Name')

    return render(
        request, "business_reports/sales_reports.html",
        {
            "sales": sales,
            "customers": customers
        },
    )

def vendorPurchaseReports(request, pk=None):
    # Search And Pagination
    active_agency = Agency.objects.all().filter(Active=True).first()
    if request.GET.get("calander_from"):
        fromdate = request.GET.get("calander_from")
        todate = request.GET.get("calander_to")
        if active_agency is not None:
            purchases = SinglePurchaseEntry.objects.filter(doc__range=[fromdate, todate],quotation__order__Agency=active_agency.id).order_by("-id")
    elif request.GET.get("search"):
        query = request.GET.get("search")
        lookups = (
                    Q(vendorId__Company_Name__icontains=query) | Q(vendorId__Vendor_Name__icontains=query) | 
                    Q(customerId__Founder_Name__icontains=query) | Q(customerId__Company_Name__icontains=query)
                )
        if active_agency is not None:
            purchases = SinglePurchaseEntry.objects.filter(lookups, quotation__order__Agency=active_agency.id).order_by("-id").distinct()
    else:
        purchases = SinglePurchaseEntry.objects.filter(quotation__order__Agency=active_agency, vendorId__id = pk).order_by("-id")

    paginator = Paginator(purchases, 10)
    purchases = paginator.page(request.GET.get("page", 1))
    vendors = Vendor.objects.all().values('id', 'Company_Name')

    return render(
        request,
        "business_reports/purchase_reports.html",
        {
            "purchases": purchases,
            "vendors": vendors,
        },
    )

def customersReports(request):
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
        "business_reports/customers_reports.html",
        {
            "salesinvoices": salesinvoices,
            "totalwgst": totalwgst,
            "totalwogst": totalwogst,
            "recivedamount": recivedamount,
            "netreciveable": netreciveable,
        },
    )

def vendorsReports(request):
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
        "business_reports/vendors_reports.html",
        {
            "salesinvoices": salesinvoices,
            "totalwgst": totalwgst,
            "totalwogst": totalwogst,
            "recivedamount": recivedamount,
            "netreciveable": netreciveable,
        },
    )
