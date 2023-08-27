from django.shortcuts import render
from apps.expences import models
from apps.agency.models import Agency
from datetime import datetime 
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def ExpencesView(request):
    active_agency = Agency.objects.all().filter(Active=True).first()
    totalamount = 0
    if request.GET.get('calander_from'):
        fromdate = request.GET.get('calander_from')
        todate = request.GET.get('calander_to')
        expences = models.Expences.objects.filter(Agency=active_agency,Date__range=[fromdate,todate])
    elif(request.GET.get('search')):
        query = request.GET.get('search') 
        expences = models.Expences.objects.filter(Q(Expence_Name__icontains=query)| Q(Expence_Category__Category__icontains=query)| Q(Payment_Mode__icontains=query),Agency=active_agency)
    else:
        expences = models.Expences.objects.filter(Agency=active_agency)

    for expence in expences:
        totalamount += int(expence.Amount)

    paginator = Paginator(expences, 10)
    expences = paginator.page(request.GET.get('page',1))
    return render(request, 'expences/expences.html',{
        'active_agency' : active_agency,
        'expence_categories' : models.ExpenceCategories.objects.all(),
        'expences':expences,
        'total' : totalamount
        })