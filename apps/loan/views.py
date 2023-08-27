from django.shortcuts import render
from apps.agency.models import Agency
from . import models
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def Loan(request):
    agency = Agency.objects.filter(Active=True).first()
    print(agency)
    if(request.GET.get('search')):
        query = request.GET.get('search')
        loans = models.Loan.objects.filter(Q(Name__icontains=query),Agency=agency).order_by('-id')
    else:
        loans = models.Loan.objects.filter(Agency=agency).order_by('-id')

    paginator = Paginator(loans, 10)
    loans = paginator.page(request.GET.get('page', 1))
    return render(request,'loan/loan.html',{
        'agency':agency,
        'loans':loans,
    })