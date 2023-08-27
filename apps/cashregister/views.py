
from django.http import HttpResponse
from . models import purchase_entry,sales_entry,sales_material,purchase_material,CashUser
from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.hashers import make_password

# Create your views here.

def cash_format(request):
    if 'username' in request.POST:
        userlist = CashUser.objects.filter(Username=request.POST['username'],Password=request.POST['password']).first()
        if userlist :
            request.session['name']='c_reg'
        return redirect('cash_format')

    if 'logut_cash' in request.POST:
        response = HttpResponseRedirect('/cash-register/')
        response.delete_cookie('sessionid')
        return response

    if 'q' in request.GET:
        q=request.GET['q']
        purchase_entry_data=purchase_entry.objects.all()
        lookups=(Q(purchase_company__icontaines=q) | Q(sales_company__icontaines=q))
        qs=purchase_entry.objects.filter(lookups)
         
        context= {
            'purchase_entry_data':qs
         }
        return render(request,'cashregister/cash_format.html',context)

    elif  'q' in request.GET:
        q=request.GET['q']
        sales_entry_data=sales_entry.objects.all()
        lookups=(Q(purchase_company__icontaines=q) | Q(sales_company__icontaines=q))
        qs=sales_entry.objects.filter(lookups)
         
        context= {
            'sales_entry_data':qs
         }
        return render(request,'cashregister/cash_format.html',context) 

    else:
        purchase_entry_data=purchase_entry.objects.all()
        sales_entry_data=sales_entry.objects.all()
        purchase_material_data=purchase_material.objects.all()
        sales_material_data=sales_material.objects.all()

        context = {
            
        'purchase_entry_data':purchase_entry_data,
        'sales_entry_data':sales_entry_data,
        'purchase_material_data':purchase_material_data,
        'sales_material_data':sales_material_data
    } 
    return render(request,'cashregister/cash_format.html',context)


def add_purchase_entry_form(request):
    if request.method=="POST":
          purchase_entry_data=purchase_entry(date=request.POST['purchase_entry_date'],
          purchase_company=request.POST['purchase_company'],
          sales_company=request.POST['sales_company'],
          billing_address=request.POST['billing_address'],
          delivery_address=request.POST['delivery_address'],
          round_off=request.POST['round_off'],
          total_quantity=request.POST['total_quantity'],
          amount=request.POST['amount'],
          amount_paid=request.POST['amount_paid'],
          amount_balance=request.POST['amount_balance'],
          voucher=request.POST['voucher'],
          dc_scan_copy=request.POST['dc_scan_copy'],
          purchase_bill=request.POST['purchase_bill']
        )
          purchase_entry_data.save()
          return redirect('cash_format')


def purchase_material_add(request,id):
    purchase_entry_data=purchase_entry.objects.filter(id=id)
    if request.method=="POST":
        mandata = purchase_material.objects.create(material=request.POST['material'],
                                                    quantity_type=request.POST['quantity_type'],
                                                    quantity=request.POST['quantity'],
                                                    price=request.POST['price'])

        purchase_entry_data[0].material.add(mandata)
        return redirect('cash_format')


def delete_purchase_entry(request,id):
    d=purchase_entry.objects.get(id=id)
    d.delete()

    return redirect('cash_format')


def delete_purchase_materials(request,id):
    d=purchase_material.objects.get(id=id)
    d.delete()

    return redirect('cash_format')


def edit_purchase_entry_form(request,id):
    if request.method=="POST":
          edit_purchase=purchase_entry.objects.filter(id=id).update(date=request.POST['purchase_entry_date'],
          purchase_company=request.POST['purchase_company'],
          sales_company=request.POST['sales_company'],
          billing_address=request.POST['billing_address'],
          delivery_address=request.POST['delivery_address'],
          round_off=request.POST['round_off'],
          total_quantity=request.POST['total_quantity'],
          amount=request.POST['amount'],
          amount_paid=request.POST['amount_paid'],
          amount_balance=request.POST['amount_balance'],
          voucher=request.POST['voucher'],
          dc_scan_copy=request.POST['dc_scan_copy'],
          purchase_bill=request.POST['purchase_bill']
        )
          return redirect('cash_format')


# SALES
def add_sale_entry_form(request):
    if request.method=="POST":
          sales_entry_data=sales_entry(sales_entry_date=request.POST['sales_entry_date'],
          purchase_company=request.POST['purchase_company'],
          sales_company=request.POST['sales_company'],
          billing_address=request.POST['billing_address'],
          delivery_address=request.POST['delivery_address'],
          round_off=request.POST['round_off'],
          total_quantity=request.POST['total_quantity'],
          amount=request.POST['amount'],
          amount_paid=request.POST['amount_paid'],
          amount_balance=request.POST['amount_balance'],
          invoice=request.POST['invoice'],
          dc_scan_copy=request.POST['dc_scan_copy']
        )
          sales_entry_data.save()
          return redirect('cash_format')



def delete_sale_entry(request,id):
    s=sales_entry.objects.get(id=id)
    s.delete()

    return redirect('cash_format')
    


def edit_sale_entry_form(request,id):
    if request.method=="POST":
          edit_sale_entry=sales_entry.objects.filter(id=id).update(sales_entry_date=request.POST['sales_entry_date'],
          purchase_company=request.POST['purchase_company'],
          sales_company=request.POST['sales_company'],
          billing_address=request.POST['billing_address'],
          delivery_address=request.POST['delivery_address'],
          round_off=request.POST['round_off'],
          total_quantity=request.POST['total_quantity'],
          amount=request.POST['amount'],
          amount_paid=request.POST['amount_paid'],
          amount_balance=request.POST['amount_balance'],
          invoice=request.POST['invoice'],
          dc_scan_copy=request.POST['dc_scan_copy']
        )


    return redirect('cash_format')




def sales_material_add(request,id):
    sales_entry_data=sales_entry.objects.filter(id=id)
    if request.method=="POST":
        mandata=sales_material.objects.create(material=request.POST['material'],
                                            quantity_type=request.POST['quantity_type'],
                                            quantity=request.POST['quantity'],
                                            price=request.POST['price'])
                                            
        sales_entry_data[0].material.add(mandata)
        return redirect('cash_format')
       

def delete_sales_materials(request,id):
    d=sales_material.objects.get(id=id)
    d.delete()

    return redirect('cash_format')
    
def purchaseapi(request,id):
    queryset=purchase_entry.objects.filter(id=id)
    ex=serializers.serialize('json',queryset,use_natural_foreign_keys=True)
    return HttpResponse(ex)

def salesapi(request,id):
    queryset=sales_entry.objects.filter(id=id)
    ex1=serializers.serialize('json',queryset,use_natural_foreign_keys=True)
    return HttpResponse(ex1)
