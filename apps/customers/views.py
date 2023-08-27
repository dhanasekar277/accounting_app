from django.shortcuts import render, redirect
from apps.customers.models import Customer
from apps.agency.models import Agency
from django.contrib import messages
from apps.customers import forms
from apps.home.models import Notification
from django.core.paginator import Paginator
from django.db.models import Q
import json
# Create your views here.


def Customers(request):
    active = Agency.objects.all().filter(Active=True)

    if(request.GET.get('search')):
        query = request.GET.get('search')
        customers = Customer.objects.filter(Q(Company_Name__icontains=query) | Q(GST_No__GST_No__icontains=query)).order_by('-id')
    else:
        customers = Customer.objects.filter(is_active=True).order_by('-id')

    paginator = Paginator(customers, 10) 
    customers = paginator.page(request.GET.get('page', 1))

    context = {
        'agency_obj' : Agency.objects.all(),
        'active_agency_obj' : active,
        'customer_obj' : customers,
    }
    return render(request, 'customers/customer.html', {'obj':context})


def Add_Customer(request):

    cf = forms.CustomerForm(request.POST, request.FILES or None)

    
    active = Agency.objects.all().filter(Active=True)
    context = {
        'agency_obj' : Agency.objects.all(),
        'active_agency_obj' : active,
        'customer_form': cf,
    }

    if request.method == 'POST':
        getColumn = list(request.POST.keys())
        # print(getColumn)
        if getColumn[1] == 'Company_Name':
            # print(getColumn[1])
            if request.POST['Company_Name'] != '':
                obj = cf.save()
                UpdateNotification(obj.id, 'customers', 'A', request.user)                
                messages.success(request, 'Customer Detail Added. !!!')
                return redirect('/customers/add-customer')
            else:
                messages.error(request, 'Founder Name detail not found. !!!') 

                

    return render(request, 'customers/customer-add.html', {'obj':context})


def Update_Customer(request, pk=None):
    customer_data = Customer.objects.get(id=pk)
    cm = forms.CustomerForm(request.POST or request.FILES or None, instance=customer_data)
    active = Agency.objects.all().filter(Active=True)
    context = {
        'cm' : cm,
        'agency_obj' : Agency.objects.all(),
        'active_agency_obj' : active,
    }

    if request.method == 'POST':

        if request.POST['Founder_Name'] != '':
            obj = cm.save()
            UpdateNotification(obj.id, 'customers', 'E', request.user)   
            messages.success(request, 'Customer Updated. !!!')
        else:
            messages.error(request, 'Customer Name is empty !!!')

    return render(request, 'customers/customer-update.html', {'obj':context})


def UpdateNotification(id, modal, type, user):

    if user.is_staff:
        Noti = {
            "id":id,
            "model":modal
        }
        obj = Notification.objects.create(Notifications=json.dumps(Noti), Types=type, User=user, Status=False)

    return obj