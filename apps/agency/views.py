from django.shortcuts import render, redirect
from django.utils.functional import empty
from apps.agency import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# specific to this view
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from apps.agency import forms
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.db.models import Q
from apps.home.models import Notification
import json
# Create your views here.

 
def Agencies(request):
    if(request.GET.get('search')):
        query = request.GET.get('search')
        agencies = models.Agency.objects.filter(Q(Name__icontains=query)).order_by('-id')
    else:
        agencies = models.Agency.objects.filter().order_by('-Timestamp')

    paginator = Paginator(agencies, 10)
    agencies = paginator.page(request.GET.get('page', 1))
    context = {
        'agency_obj' : agencies,
        'active_agency_obj' : models.Agency.objects.all().filter(Active=True),
    }
    return render(request, 'agencies/agency.html', {'obj':context})


def Add_Agency(request):

    fm = forms.AgencyForm(request.POST, request.FILES or None)

    context = {
        'fm' : fm,
        'agency_obj' : models.Agency.objects.all(),
        'active_agency_obj' : models.Agency.objects.all().filter(Active=True),
    }

    if request.method == 'POST':
        # get columns as keys
        getColumn = list(request.POST.keys())
        # check account submit
        # print(getColumn)
        if getColumn[1] == 'Name':
            if not models.Agency.objects.filter(Name=request.POST['Name']) and request.POST['Name'] != '':
                obj = fm.save()
                UpdateNotification(obj.id, 'agency', 'A', request.user)
                messages.success(request, 'Agency Added. !!!')
                return redirect('/agencies/add-agency')
            else:
                messages.error(request, 'Agency Name is empty or already exists. !!!') 

        return render(request, 'agencies/add-agency.html', {'obj':context})

    else:

        return render(request, 'agencies/add-agency.html', {'obj':context})

 
def Update_Agency(request, pk=None):

    agency_data =  models.Agency.objects.get(id=pk)
    fm = forms.AgencyForm(request.POST or request.FILES or None, instance=agency_data)

    context = {
        'fm' : fm,
        'agency_obj' : models.Agency.objects.all(),
        'active_agency_obj' : models.Agency.objects.all().filter(Active=True),
    }

    if request.method == 'POST':

        if request.POST['Name'] != '':
            obj = fm.save()
            messages.success(request, 'Agency Updated. !!!')
        else:
            messages.error(request, 'Agency Name is empty !!!')

        return render(request, 'agencies/update-agency.html', {'obj':context})

    return render(request, 'agencies/update-agency.html', {'obj':context})



def updateagency(request, pk=None):
    allagency = models.Agency.objects.update(Active=False)
    updatebyidagency = models.Agency.objects.filter(id=pk).update(Active=True)
    return JsonResponse({'status':200, 'message':'Agency updated. !!!'})


def UpdateNotification(id, modal, type, user):

    if user.is_staff:
        Noti = {
            "id":id,
            "model":modal
        }
        obj = Notification.objects.create(Notifications=json.dumps(Noti), Types=type, User=user, Status=False)

    return obj
