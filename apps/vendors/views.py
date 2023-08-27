from cgitb import lookup
from django.shortcuts import render, redirect
from apps.vendors.models import Vendor
from apps.agency.models import Agency
from apps.vendors import forms
from django.contrib import messages
from apps.home.models import Notification
from django.core.paginator import Paginator
from django.db.models import Q
import json
# Create your views here.
 
def Vendors(request):
    if(request.GET.get('search')):
        query = request.GET.get('search')
        lookups = Q(Company_Name__icontains=query) | Q(Vendor_Name__icontains=query) | Q(GST_No__GST_No__icontains=query) | Q(Material_Supplying__Material_Name__icontains=query)
        vendors = Vendor.objects.filter(lookups).order_by('-id').distinct()
    else:
        vendors = Vendor.objects.filter(is_active=True).order_by('-id')

    paginator = Paginator(vendors, 10)
    vendors = paginator.page(request.GET.get('page', 1))

    context = {
        'vendor_obj' : vendors
    }
    return render(request, 'vendors/vendors.html', {'obj':context})
 

def Add_Vendor(request):

    vf = forms.VendorForm(request.POST or None)
    context = {
        'vendor_form': vf,
    }   

    if request.method == 'POST':
        getColumn = list(request.POST.keys())
        getvalues = list(request.POST.values())

        if request.POST['Vendor_Name'] != '':
            obj = vf.save()
            UpdateNotification(obj.id, 'vendors', 'A', request.user)                
            messages.success(request, ' Vendor Detail Added. !!!')
            return redirect('/vendors/add-vendor/')
        else:
            messages.error(request, 'Vendor detail not found. !!!') 

                

    return render(request, 'vendors/vendor_add.html', {'obj':context})


def Update_Vendor(request, pk=None):

    vendor_data =  Vendor.objects.get(id=pk)
    vf = forms.VendorForm(request.POST or request.FILES or None, instance=vendor_data)
    
    active = Agency.objects.all().filter(Active=True)
    context = {
        'agency_obj' : Agency.objects.all(),
        'active_agency_obj' : active,
        'vendor_form': vf,
    }

    if request.method == 'POST':

        if request.POST['Vendor_Name'] != '':
            obj = vf.save()
            UpdateNotification(obj.id, 'vendors', 'E', request.user)   
            messages.success(request, 'Vendor Updated. !!!')
        else:
            messages.error(request, 'Vendor Name is empty !!!')

        return render(request, 'vendors/update-vendor.html', {'obj':context})

    return render(request, 'vendors/update-vendor.html', {'obj':context})


def UpdateNotification(id, modal, type, user):
    if user.is_staff:
        Noti = {
            "id":id,
            "model":modal
        }
        obj = Notification.objects.create(Notifications=json.dumps(Noti), Types=type, User=user, Status=False)
    return obj
