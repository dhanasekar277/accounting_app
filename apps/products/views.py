from django.shortcuts import render, HttpResponse
from apps.agency.models import Agency
from apps.products.models import Product
from django.core.paginator import Paginator
from django.db.models import Q
from django.core import serializers

from apps.vendors.models import Vendor

# Create your views here.
def Products(request):
    if(request.GET.get('search')):
        query = request.GET.get('search')
        products = Product.objects.values('Product').distinct().filter(Q(Product__icontains=query)).order_by('-id')
    else:
        products = Product.objects.values('Product').distinct()

    paginator = Paginator(products, 10)
    products = paginator.page(request.GET.get('page', 1))

    active = Agency.objects.all().filter(Active=True)
    context = {
        'active_agency_obj' : active,
        'product_obj' : products
    }
    return render(request, 'products/product.html', {'obj':context})

def productViewApi(request,name):
    queyset = Product.objects.filter(Product=name)
    products = serializers.serialize('json',queyset, use_natural_foreign_keys=True,
    fields = ['Product','Material_Type','Material_Supplying','HSNCode','GST','Vendor'])
    return HttpResponse(products)