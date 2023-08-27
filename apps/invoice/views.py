from django.shortcuts import render
from apps.sales.models import Sales, SalesCollection
from apps.invoice.models import SalesInvoice, SingleSalesInvoice
from django.http import HttpResponse, JsonResponse
from django.core import serializers
# Create your views here.
  
def Invoice(request, pk):
    context = {
        'sales': SalesCollection.objects.get(orderid=pk),
        'AutoInvoiceNo': SingleSalesInvoice.objects.filter(orderid=pk),
    }

    return render(request, 'invoice/sales-invoice.html', context)


def GetLatestInvoice(request):
    invoice_id = SingleSalesInvoice.objects.order_by('-id')[:1]
    json_res = serializers.serialize('json',invoice_id) 
    return JsonResponse(json_res, safe=False)