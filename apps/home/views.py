from inspect import signature
import re
import shutil
from django.contrib.auth.hashers import make_password
from typing import Counter
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from apps.vendors.models import Vendor, VendorStaffDetail
from apps.products.models import Product
from django.core.paginator import Paginator
from apps.agency.models import Agency, Signature
from apps.customers.models import Customer
from apps.home.models import FileManagement as multifiles
from apps.home.models import Notification
from django.contrib.auth.models import User
import calendar
from datetime import datetime
from apps.purchase.models import PurchaseEntry 
from apps.voucher.models import VoucherDetail , Voucher
from apps.invoice.models import SalesInvoice, SingleSalesInvoice
from apps.orders.models import Order
from apps.sales.models import SalesCollection
from apps.expences.models import Expences
from itertools import chain
from django.db.models import Q, Sum
import os
import pathlib
from apps.home.models import FileManagement
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.core import serializers
# Create your views here.
  
def home(request):
    active_agency = Agency.objects.all().filter(Active=True).first()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {"error": "Invalid username or password."}
            return render(request, '_index.html', context)
        login(request, user) 
        return redirect('/')
    chart_data = []
    current_month = datetime.now().month-1

    for i in range(1,13):
        chart_data.append([calendar.month_name[i],VoucherDetail.objects.filter(Date__month=(i)).aggregate(Sum('amount__total_amount')).get('amount__total_amount__sum'),
        SalesInvoice.objects.filter(Date__month=(i)).aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount')).get('saleid__sales__netAmount__WithGSTNetTotalAmount__sum')])

    return render(request, '_index.html',{
        'chart_data' : chart_data,
        'recent_orders' : Order.objects.filter(Agency=active_agency).order_by('-id')[:5],
        'recent_customers' : Customer.objects.all().order_by('-id')[:5],
        'recent_vendors' : Vendor.objects.all().order_by('-id')[:5],
        'recent_invoices' : SingleSalesInvoice.objects.filter(orderid__Agency=active_agency).order_by('-id')[:5],
        'recent_products' : Product.objects.all().order_by('-id').distinct()[:5],
    })


def phonebooks(request):

    active = Agency.objects.all().filter(Active=True)
    context = {
        'agency_obj' : Agency.objects.all(),
        'active_agency_obj' : active,
        'customer_obj' : Customer.objects.filter(),
    }

    return render(request, 'phonebook/phonebook.html', {'obj':context})


def gst_details(request):
    """ SALES """
    active_agency = Agency.objects.all().filter(Active=True).first()
    # Search And PAgination
    if request.GET.get('sales_calander_from'):
        fromdate = request.GET.get('sales_calander_from')
        todate = request.GET.get('sales_calander_to')
        if active_agency is not None:
            salesinvoices = SalesInvoice.objects.filter(Date__range=[fromdate,todate],saleid__orderid__Agency=active_agency.id).order_by('-id')
    elif(request.GET.get('sales_search')):
        query = request.GET.get('sales_search')
        lookups = Q(saleid__sales__customer__customerid__Company_Name__icontains=query)
        if active_agency is not None:
            salesinvoices = SalesInvoice.objects.filter(lookups, saleid__orderid__Agency=active_agency.id).order_by('-id')
    else:
        salesinvoices = SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency.id).order_by('-id')

    # Total Net Sales Start
    salestotalwgst = salesinvoices.aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
    salestotalwogst = salesinvoices.aggregate(Sum('saleid__sales__netAmount__WithOutGSTNetTotalAmount'))
    # Total Net Sales END

    paginator = Paginator(salesinvoices, 10)
    salesinvoices = paginator.page(request.GET.get('page', 1))

    """ PURCHASE """
    # Search And PAgination
    if request.GET.get('purchase_calander_from'):
        fromdate = request.GET.get('purchase_calander_from')
        todate = request.GET.get('purchase_calander_to')
        if active_agency is not None:
            voucherdetails = Voucher.objects.filter(Date__range=[fromdate,todate],quotation__agency=active_agency.id).order_by('-id')
    elif(request.GET.get('purchase_search')):
        query = request.GET.get('purchase_search') 
        lookups1 = Q(voucher__vendorDetail__Name__icontains=query) 
        if active_agency is not None:
            voucherdetails = Voucher.objects.filter(lookups1, quotation__agency=active_agency.id).order_by('-id')
    else:
        voucherdetails = Voucher.objects.filter(quotation__agency=active_agency.id).order_by('-id')

    # Total Net Sales Start
    purchasetotalwgst = voucherdetails.aggregate(Sum('voucher__amount__total_amount'))
    purchasetotalwogst = voucherdetails.aggregate(Sum('voucher__amount__total'))
    purchasesgstamount = voucherdetails.aggregate(Sum('voucher__amount__sgst_amount'))
    purchasecgstamount = voucherdetails.aggregate(Sum('voucher__amount__cgst_amount'))
    purchasetotalnetpaid = voucherdetails.aggregate(Sum('purchase__entries__netAmount__AmountPayyed'))
    purchasetotalnetbalance = voucherdetails.aggregate(Sum('purchase__entries__netAmount__Balance'))

    paginator = Paginator(voucherdetails, 10)
    voucherdetails = paginator.page(request.GET.get('page', 1))

    return render(request, 'gst/gst-detail.html',{
        # sales
        'salesinvoices':salesinvoices,
        'salestotalwgst':salestotalwgst,
        'salestotalwogst':salestotalwogst,
        'salesgst' : SalesInvoice.objects.values_list('invoice__orderid__Materials__Product_Name__GST'),
        # purchase
        'voucherdetails':voucherdetails,
        'purchasetotalwgst':purchasetotalwgst,
        'purchasetotalwogst':purchasetotalwogst,
        'purchasesgstamount':purchasesgstamount,
        'purchasecgstamount':purchasecgstamount,
        'purchasetotalnetpaid':purchasetotalnetpaid,
        'purchasetotalnetbalance':purchasetotalnetbalance,
    })


def businessReport(request):
    """ SALES """
    active_agency = Agency.objects.all().filter(Active=True).first()
    # Search And PAgination
    if request.GET.get('sales_calander_from'):
        fromdate = request.GET.get('sales_calander_from')
        todate = request.GET.get('sales_calander_to')
        if active_agency is not None:
            salesinvoices = SalesInvoice.objects.filter(Date__range=[fromdate,todate],saleid__orderid__Agency=active_agency.id).order_by('-id')
    elif(request.GET.get('sales_search')):
        query = request.GET.get('sales_search')
        lookups = Q(saleid__sales__customer__customerid__Company_Name__icontains=query)
        if active_agency is not None:
            salesinvoices = SalesInvoice.objects.filter(lookups, saleid__orderid__Agency=active_agency.id).order_by('-id')
    else:
        salesinvoices = SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency.id).order_by('-id')

    # Total Net Sales Start
    salestotalwgst = salesinvoices.aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
    salestotalwogst = salesinvoices.aggregate(Sum('saleid__sales__netAmount__WithOutGSTNetTotalAmount'))
    # Total Net Sales END

    paginator = Paginator(salesinvoices, 10)
    salesinvoices = paginator.page(request.GET.get('page', 1))

    """ PURCHASE """
    # Search And PAgination
    if request.GET.get('purchase_calander_from'):
        fromdate = request.GET.get('purchase_calander_from')
        todate = request.GET.get('purchase_calander_to')
        if active_agency is not None:
            voucherdetails = Voucher.objects.filter(Date__range=[fromdate,todate],quotation__agency=active_agency.id).order_by('-id')
    elif(request.GET.get('purchase_search')):
        query = request.GET.get('purchase_search') 
        lookups1 = Q(voucher__vendorDetail__Name__icontains=query) 
        if active_agency is not None:
            voucherdetails = Voucher.objects.filter(lookups1, quotation__agency=active_agency.id).order_by('-id')
    else:
        voucherdetails = Voucher.objects.filter(quotation__agency=active_agency.id).order_by('-id')

    # Total Net Sales Start
    purchasetotalwgst = voucherdetails.aggregate(Sum('voucher__amount__total_amount'))
    purchasetotalwogst = voucherdetails.aggregate(Sum('voucher__amount__total'))
    purchasesgstamount = voucherdetails.aggregate(Sum('voucher__amount__sgst_amount'))
    purchasecgstamount = voucherdetails.aggregate(Sum('voucher__amount__cgst_amount'))
    purchasetotalnetpaid = voucherdetails.aggregate(Sum('purchase__entries__netAmount__AmountPayyed'))
    purchasetotalnetbalance = voucherdetails.aggregate(Sum('purchase__entries__netAmount__Balance'))

    paginator = Paginator(voucherdetails, 10)
    voucherdetails = paginator.page(request.GET.get('page', 1))

    return render(request, 'gst/business-reports.html',{
        # sales
        'salesinvoices':salesinvoices,
        'salestotalwgst':salestotalwgst,
        'salestotalwogst':salestotalwogst,
        'salesgst' : SalesInvoice.objects.values_list('invoice__orderid__Materials__Product_Name__GST'),
        # purchase
        'voucherdetails':voucherdetails,
        'purchasetotalwgst':purchasetotalwgst,
        'purchasetotalwogst':purchasetotalwogst,
        'purchasesgstamount':purchasesgstamount,
        'purchasecgstamount':purchasecgstamount,
        'purchasetotalnetpaid':purchasetotalnetpaid,
        'purchasetotalnetbalance':purchasetotalnetbalance,
    })

 
def FileManagement(request):
    vendor = Vendor.objects.all().only("Company_Name")
    customer = Customer.objects.all().only("Company_Name")
    names = chain(vendor, customer)

    if request.FILES:
        for f in request.FILES.getlist('filemanage'):
            uploadFile = multifiles.objects.create(File=f)
    filedata = multifiles.objects.all().order_by('-timestamp')
    return render(request,'filemanagement/filemanagement.html',{
    'filedata':filedata,
    'names': names,
    })


def path_to_dict(request):
    
    original_path = pathlib.Path(__file__).parent.resolve()
    print(original_path)
    original_path = str(original_path).split("apps")[0]
    path = original_path + 'media/file-manager'
    # path.replaceAll('\\','/')
    print(path)
    # path = 'C:/Users/Surendar/Desktop/agency/server/agencies/media/file-manager'
    print(path)
    d = {'name': os.path.basename(path)}
    files = []
    file_name = []
    for x in os.listdir(path):
        file_name.append(x)
        y = path+'/'+x
        files.append(y)
    d['file_name'] = file_name
    d['dir'] = files
    return JsonResponse(d)

def folder_path_files(request, folder_name):

    original_path = GetPath(folder_name)
    d = {'name': os.path.basename(original_path)}

    files = []
    file_name = []
    for x in os.listdir(original_path):
        file_name.append(x)
        y = original_path+'/'+x
        files.append(y)
    d['file_name'] = file_name
    d['dir'] = files

    return JsonResponse(d)

 
def createFolder(request, name, path):
    folder_path = GetPath(path)
    folder_name = name
    # folder_path = '/home/vingsfire/accounting-app/media/file-manager/'
    path = os.path.join(folder_path, folder_name)
    # path = '/home/vingsfire/accounting-app/media/file-manager/'+name
    os.mkdir(path)
    # return HttpResponse(path)
    return JsonResponse({'success':'Folder Created Successfully. !!!', 'path':folder_path, 'name':folder_name})

        
def GetPath(name):
    original_path = pathlib.Path(__file__).parent.resolve()
    original_path = str(original_path).split("apps")[0]
    if name == 'file-manager':
        original_path = original_path + 'media/'+name
        print('work')
    else:
        print(name)
        name = name.replace('-', '/')
        name = name.replace('Home', '')
        # print(name)
        original_path = original_path + 'media/file-manager/'+name
    return original_path

 
# delete file request
def DeleteFile(request, path):
    path = path.replace('_-_-_', ':')
    # print(path)
    path = path.replace('--', '/')
    print(path)
    # print(os.path.exists(path))
    if os.path.exists(path):
        os.remove(path)
        return JsonResponse({'success':'Deleted Successfully. !!!'})
    else:
        return JsonResponse({'success':'Failed. !!!'})


def uploadFile(request):
    if request.method == 'POST':
        file_name = request.FILES['file_name']
        file_path = request.POST['file_path']
        get_absolute_path = uploadPath(file_path)

        fs = FileSystemStorage()
        filename = fs.save(file_name.name, file_name)
        # print(filename)
        uploaded__file__url = fs.url(filename)
        path = pathlib.Path(__file__).parent.resolve()
        path = str(path).split("apps")[0]
        uploaded__file__url = path + 'media/' + filename
        # print(uploaded__file__url)

        shutil.move(uploaded__file__url, get_absolute_path)
        return redirect(FileManagement)

def uploadPath(file_path):
    original_path = pathlib.Path(__file__).parent.resolve()
    original_path = str(original_path).split("apps")[0]
    file_path = file_path.replace('___', '/')
    original_path = original_path + 'media/' + file_path
    return original_path


def BalanceConformationLetter(request):
    active_agency = Agency.objects.all().filter(Active=True).first()
    if(request.GET.get('search')):
        query = request.GET.get('search')
        lookups = Q(saleid__sales__customer__customerid__Company_Name__icontains=query) 
        if active_agency is not None:
            salesinvoices = SalesInvoice.objects.filter(lookups, saleid__orderid__Agency=active_agency.id).order_by('-id')
    else:
        salesinvoices = SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency).order_by('-id')

    recivedamount = salesinvoices.aggregate(Sum('saleid__sales__netAmount__AmountPayyed'))
    netreciveable = salesinvoices.aggregate(Sum('saleid__sales__netAmount__Balance'))

    paginator = Paginator(salesinvoices, 10)
    salesinvoices = paginator.page(request.GET.get('page', 1))

    return render(request, 'balance_conformation/bcl.html',{
        'salesinvoices':salesinvoices,
        'recivedamount':recivedamount,
        'netreciveable':netreciveable,
        'active_agency_obj' : Agency.objects.all().filter(Active=True),
    })


def DashboardDetails(request):
    active_agency = Agency.objects.all().filter(Active=True).first()
    orders = {}
    customers = {}
    vendors = {}
    products = {}
    invoices = {}

    for i in Order.objects.filter(Agency=active_agency).order_by('-id')[:5]:
        orders[i.id] = {
            'Founder_Name' : i.Sales_Company.Founder_Name,
            'Company_Name' : i.Sales_Company.Company_Name,
            'Status' : i.Approved,
        }
    
    for i in Customer.objects.all().order_by('-id')[:5]:
        customers[i.id] = {
            'Founder_Name' : i.Founder_Name,
            'Company_Name' : i.Company_Name,
            'Email' : i.Founder_Email,
            # 'Phone' : i.Founder_Phone,
            'Status' : i.is_active,
        }
    
    for i in Vendor.objects.all().order_by('-id')[:5]:
        vendors[i.id] = {
            'Name' : i.Vendor_Name,
            'Company_Name' : i.Company_Name,
            'No_Of_Trucks' : i.No_Of_Trucks,
            'Email' : i.Email,
            'Phone' : i.Phone,
            'Status' : i.is_active,
        }
    
    for i in Product.objects.all().order_by('-id')[:5]:
        products[i.id] = {
            'Product' : i.Product,
            'Material_Type' : i.Material_Type,
            'Vendor' : i.Vendor.Vendor_Name,
            'GST' : i.GST,
            'HSNCode' : i.HSNCode,
        }
    
    for i in SingleSalesInvoice.objects.filter(orderid__Agency=active_agency).order_by('-id')[:5]:
        invoices[i.id] = {
            'InvoiceNo' : i.InvoiceNo,
            'Destination' : i.Destination,
            'InvoiceDate' : i.InvoiceDate,
            'Total' : i.saleid.netAmount.WithGSTNetTotalAmount,
            'Balance_amount' : i.saleid.netAmount.Balance,
        }

    dashboarddata = {
        'totalorders': Order.objects.filter(Agency=active_agency).count(),
        'totalpurchase': PurchaseEntry.objects.filter(quotation__agency=active_agency).count(),
        'totalsales': SalesCollection.objects.filter(orderid__Agency=active_agency).count(),
        'totalinvoice': SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency).count(),
        'totalpayable': Voucher.objects.filter(quotation__agency=active_agency).aggregate(Sum('purchase__entries__netAmount__Balance')).get('purchase__entries__netAmount__Balance__sum'),
        'totalreciveable': SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency).aggregate(Sum('saleid__sales__netAmount__Balance')).get('saleid__sales__netAmount__Balance__sum'),
        'neworders': Order.objects.filter(Agency=active_agency,Date__month=(datetime.now().month)).count(),
        'sales' : {
            'previous_month' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__month=(datetime.now().month-1)).aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount')),
            'current_month' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__month=(datetime.now().month)).aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
        },
        'purchase' : {
            'previous_month' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__month=(datetime.now().month-1)).aggregate(Sum('amount__total_amount')),
            'current_month' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__month=(datetime.now().month)).aggregate(Sum('amount__total_amount'))
        },
        'recent_orders' : orders,
        'recent_customers' : customers,
        'recent_vendors' : vendors,
        'recent_products' : products,
        'recent_invoices' : invoices,
    }

    return JsonResponse(dashboarddata)


def Settings(request):
    superuser = User.objects.filter(is_superuser=True, is_active=True)
    users = User.objects.filter(is_staff=True, is_superuser=False, is_active=True)
    signatures = Signature.objects.all().order_by('-id')
    obj = {
        'classname' : 'd-none',
    }
    context = {
        'superuser' : superuser,
        'users' : users,
        'signatures' : signatures,
        'response' : obj
    }

    if (request.POST.get('superuser_first_name')):
        if (request.POST.get('superuser_newpassword')==request.POST.get('superuser_confirmpassword')):
            print(request.POST.get('superuserid'))
            User.objects.filter(id=request.POST.get('superuserid')).update(first_name=request.POST['superuser_first_name'],
            last_name=request.POST['superuser_last_name'],
            username=request.POST['superuser_username'],
            email=request.POST['superuser_email'],
            password=make_password(request.POST['superuser_confirmpassword']),
            )
        else:
            obj['classname'] = ''
            obj['message'] = 'Password are not same'

    if (request.POST.get('user_first_name')):
        if (request.POST.get('user_newpassword')==request.POST.get('user_confirmpassword')):
            User.objects.create(first_name=request.POST['user_first_name'],
            last_name=request.POST['user_last_name'],
            username=request.POST['user_username'],
            email=request.POST['user_email'],
            password=make_password(request.POST['user_confirmpassword']),
            is_superuser=False,
            is_staff=True,
            is_active=True,
            )
        else:
            obj['classname'] = ''
            obj['message'] = 'Password are not same'

    if (request.POST.get('edituser_first_name')):
        if (request.POST.get('edituser_newpassword')==request.POST.get('edituser_confirmpassword')):
            User.objects.filter(id=request.POST.get('edituser_userid')).update(
            first_name=request.POST['edituser_first_name'],
            last_name=request.POST['edituser_last_name'],
            username=request.POST['edituser_username'],
            email=request.POST['edituser_email'],
            password=make_password(request.POST['edituser_confirmpassword']),
            )
        else:
            obj['classname'] = ''
            obj['message'] = 'Password are not same'

    return render(request, 'settings/settings.html',context)

def NotificationsCount(request):
    datacount = serializers.serialize('json',Notification.objects.filter(Change=False))
    return HttpResponse(datacount)