from django.shortcuts import render
from apps.agency.models import Agency
from apps.orders.models import Order, MaterialOrder
from apps.sales.models import Sales, SalesCollection
from apps.invoice.models import SalesInvoice, SalesMaterialInfo, SingleSalesInvoice
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


def SaleView(request):
    active_agency = Agency.objects.all().filter(Active=True).first()
    if request.GET.get("search"):
        query = request.GET.get("search")
        lookups = Q(sales__customer__customerid__Company_Name__icontains=query) | Q(sales__customer__customerid__Founder_Name__icontains=query)
        if active_agency is not None:
            sales = SalesCollection.objects.filter(lookups,orderid__Agency=active_agency.id).order_by("-id").distinct()
    else:
        sales = SalesCollection.objects.filter(orderid__Agency=active_agency).order_by("-id").distinct()

    paginator = Paginator(sales, 10)
    sales = paginator.page(request.GET.get("page", 1))

    context = {
        "sales": sales,
        "AutoInvoiceNo" : SingleSalesInvoice.objects.all(),
    }
    return render(request, "sales/sales.html", context)


def SalesEntry(request, pk):
    order = Order.objects.get(id=pk)
    context = {"order": order}
    return render(request, "sales/sales-entry.html", context)


def SalesView(request, pk):
    sales = Sales.objects.get(orderid=pk)
    context = {"sales": sales}

    return render(request, "sales/sales-view.html", context)


def GetSaleMaterial(request, pk):
    particular_expence = serializers.serialize(
        "json", SalesMaterialInfo.objects.filter(orderId=pk)
    )
    return HttpResponse(particular_expence)
