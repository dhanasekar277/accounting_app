from django.shortcuts import render
from apps.customers.models import Customer
from apps.agency.models import Agency
from apps.orders.models import Order
from apps.products.models import Product
from apps.orders import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def Orders(request):
    active_agency = Agency.objects.all().filter(Active=True).first()
    # PAGINATION
    if 'orders' in request.GET:
        # SEARCH
        ordersearch = request.GET.get('orders')
        lookups = Q(Sales_Company__Founder_Name__icontains=ordersearch) | Q(Sales_Company__Company_Name__icontains=ordersearch) | Q(PO_Number__PO_Number__icontains=ordersearch)
        if active_agency is not None:
            Order_list = Order.objects.all().filter(lookups, Agency=active_agency.id).order_by('-id')
    else:
        Order_list = Order.objects.all().filter(Agency=active_agency).order_by('-id')
    paginator = Paginator(Order_list, 10)
    orders = paginator.page(request.GET.get('page', 1))

    context = {
        'agency_obj' : Agency.objects.all(),
        'order_obj' : orders,
    }
    return render(request, 'orders/orders.html', {'obj':context})


def AddOrder(request):
    context = {
        'product_obj' : Product.objects.values('id','Product').values_list('Product', flat=True).distinct(),
        'customer_obj' : Customer.objects.all(),
        'mf': forms.MaterialOrderForm(request.POST or None)
    }
    
    return render(request, 'orders/add-order.html', {'obj':context})


def PurchaseOrder(request, id):
    context = {
        'order' : Order.objects.get(id=id),
    }
    return render(request, 'orders/purchase-order.html', context)
    

def EditOrder(request):
    return render(request, 'orders/edit-order.html')