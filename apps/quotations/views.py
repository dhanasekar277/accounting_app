from django.shortcuts import render
from apps.orders.models import Order
from apps.agency.models import Agency
from apps.quotations.models import Quotation
import json
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.


def Quotations(request):
    active_agency = Agency.objects.all().filter(Active=True).first()
    # print(active_agency)
    if(request.GET.get('search')):
        query = request.GET.get('search')
        lookups = Q(customerInfo__detail__customerName__icontains=query)
        if active_agency is not None:
            quotation = Quotation.objects.filter(lookups, agency=active_agency.id).order_by('-id')
    else:
        quotation = Quotation.objects.filter(agency=active_agency).order_by('-id')

    paginator = Paginator(quotation, 10) 
    quotation = paginator.page(request.GET.get('page', 1))

    context = {
        'quotations': quotation
    }
    return render(request, 'quotation/quotation.html', context)


def AddQuotations(request):
    active_agency = Agency.objects.all().filter(Active=True)
    context= {
        'order_obj' : Order.objects.all().filter(Agency=active_agency[0].id, Approved = True),
    }

    return render(request, 'quotation/add_quotation.html', {'obj': context})