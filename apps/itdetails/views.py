from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from apps.expences.models import Expences, ExpenceCategories
from apps.invoice.models import SalesInvoice,SingleSalesInvoice
from apps.voucher.models import VoucherDetail,PurchaseInfo
from apps.bankentries.models import BankEntry
from apps.agency.models import Agency
from django.db.models import Q, Sum 
from django.core.serializers.json import Serializer
from django.db.models import Manager

 
# Create your views here.

JSON_ALLOWED_OBJECTS = (dict,list,tuple,str,int,bool)

class CustomSerializer(Serializer):
    def end_object(self, obj):
        for field in self.selected_fields:
            if field == 'pk':
                continue
            elif field in self._current.keys():
                continue
            else:
                try:
                    if '__' in field:
                        fields = field.split('__')
                        value = obj
                        for f in fields:
                            value = getattr(value, f)
                        if value != obj and isinstance(value, JSON_ALLOWED_OBJECTS) or value == None:
                            self._current[field] = value

                except AttributeError:
                    pass
        super(CustomSerializer, self).end_object(obj)


def ItDetails(request):
    active_agency = Agency.objects.all().filter(Active=True).first()
    context = {}
    if request.GET.get('calander_from'):
        fromdate = request.GET.get('calander_from')
        todate = request.GET.get('calander_to')

 # INDIRECT EXPENCE
        expencesobj = []
        categories = ExpenceCategories.objects.filter(Agency=active_agency)
        for i in categories:
            expencesobj.append({
            'name' : i.Category,
            'value': Expences.objects.filter(Agency=active_agency,Date__range=[fromdate,todate], Payment_Type='In Direct',Expence_Category__Category=i.Category).aggregate(Sum('Amount'))
            })

        # DIRECT EXPENCES
        direct_expencesobj = []
        categories = ExpenceCategories.objects.filter(Agency=active_agency)
        for i in categories:
            direct_expencesobj.append({
            'name' : i.Category,
            'value': Expences.objects.filter(Agency=active_agency,Date__range=[fromdate,todate], Payment_Type='Direct',Expence_Category__Category=i.Category).aggregate(Sum('Amount'))
            })
        
        # SALES
        salesobj = [
            {
                'month' : 'April',
                'month_num' : '04',
                'value' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate],Date__month='04').aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
            },
            {
                'month' : 'May',
                'month_num' : '05',
                'value' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate],Date__month='05').aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
            },
            {
                'month' : 'June',
                'month_num' : '06',
                'value' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate],Date__month='06').aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
            },
            {
                'month' : 'July',
                'month_num' : '07',
                'value' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate],Date__month='07').aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
            },
            {
                'month' : 'August',
                'month_num' : '08',
                'value' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate],Date__month='08').aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
            },
            {
                'month' : 'September',
                'month_num' : '09',
                'value' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate],Date__month='09').aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
            },
            {
                'month' : 'October',
                'month_num' : '10',
                'value' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate],Date__month='10').aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
            },
            {
                'month' : 'November',
                'month_num' : '11',
                'value' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate],Date__month='11').aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
            },
            {
                'month' : 'December',
                'month_num' : '12',
                'value' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate],Date__month='12').aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
            },
            {
                'month' : 'January',
                'month_num' : '01',
                'value' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate],Date__month='01').aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
            },
            {
                'month' : 'February',
                'month_num' : '02',
                'value' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate],Date__month='02').aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
            },
            {
                'month' : 'March',
                'month_num' : '03',
                'value' : SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate],Date__month='03').aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
            }
        ]

        # PURCHASE
        purchaseobj = [
            {
                'month' : 'April',
                'month_num' : '04',
                'value' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate],Date__month='04').aggregate(Sum('amount__total_amount'))
            },
            {
                'month' : 'May',
                'month_num' : '05',
                'value' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate],Date__month='05').aggregate(Sum('amount__total_amount'))
            },
            {
                'month' : 'June',
                'month_num' : '06',
                'value' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate],Date__month='06').aggregate(Sum('amount__total_amount'))
            },
            {
                'month' : 'July',
                'month_num' : '07',
                'value' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate],Date__month='07').aggregate(Sum('amount__total_amount'))
            },
            {
                'month' : 'August',
                'month_num' : '08',
                'value' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate],Date__month='08').aggregate(Sum('amount__total_amount'))
            },
            {
                'month' : 'September',
                'month_num' : '09',
                'value' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate],Date__month='09').aggregate(Sum('amount__total_amount'))
            },
            {
                'month' : 'October',
                'month_num' : '10',
                'value' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate],Date__month='10').aggregate(Sum('amount__total_amount'))
            },
            {
                'month' : 'November',
                'month_num' : '11',
                'value' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate],Date__month='11').aggregate(Sum('amount__total_amount'))
            },
            {
                'month' : 'December',
                'month_num' : '12',
                'value' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate],Date__month='12').aggregate(Sum('amount__total_amount'))
            },
            {
                'month' : 'January',
                'month_num' : '01',
                'value' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate],Date__month='01').aggregate(Sum('amount__total_amount'))
            },
            {
                'month' : 'February',
                'month_num' : '02',
                'value' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate],Date__month='02').aggregate(Sum('amount__total_amount'))
            },
            {
                'month' : 'March',
                'month_num' : '03',
                'value' : VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate],Date__month='03').aggregate(Sum('amount__total_amount'))
            }
        ]

        # SUNDRY CREDITORS
        sundry_creditors_obj = []
        Total_creditors_balance = 0
        creditors_total = 0
        sundry_creditors = BankEntry.objects.filter(agency=active_agency,Date__range=[fromdate,todate],Person_Type="vendor").values('Name','voucherId').distinct()

        for i in sundry_creditors:
            total_creditors_amount = BankEntry.objects.filter(agency=active_agency,Date__range=[fromdate,todate],Person_Type="vendor",Name=i['Name'],voucherId=i['voucherId']).values_list('Total_Amount').distinct().aggregate(Sum('Total_Amount')).get('Total_Amount__sum') or 0
            voucher_number = PurchaseInfo.objects.filter(id=i['voucherId'])
            totalNetAmount = BankEntry.objects.filter(Date__range=[fromdate,todate],Person_Type="vendor",Name=i['Name'],voucherId=i['voucherId']).order_by('-id').aggregate(Sum('Net_Balance_Paid')).get('Net_Balance_Paid__sum') or 0
            totalGSTAmount = BankEntry.objects.filter(Date__range=[fromdate,todate],Person_Type="vendor",Name=i['Name'],voucherId=i['voucherId']).order_by('-id').aggregate(Sum('GST_Balance_Paid')).get('GST_Balance_Paid__sum') or 0
            entries_trans_amount = totalNetAmount + totalGSTAmount
            net_balance = total_creditors_amount - entries_trans_amount

            sundry_creditors_obj.append({
            'name' : i['Name'],
            'voucherid' : voucher_number,
            'total' : total_creditors_amount,
            'net_balance' : net_balance,
            })
            Total_creditors_balance += net_balance
            creditors_total += total_creditors_amount

        # SUNDRY DEBITORS
        sundry_debitors_obj = []
        Total_debitors_balance = 0
        debitors_total = 0
        sundry_debitors = BankEntry.objects.filter(agency=active_agency,Date__range=[fromdate,todate],Person_Type="customer").values('Name','InvoiceId').distinct()

        for i in sundry_debitors:
            total_debitors_amount = BankEntry.objects.filter(agency=active_agency,Date__range=[fromdate,todate],Person_Type="customer",Name=i['Name'],InvoiceId=i['InvoiceId']).values_list('Total_Amount').distinct().aggregate(Sum('Total_Amount')).get('Total_Amount__sum') or 0
            invoice = SingleSalesInvoice.objects.filter(id=i['InvoiceId'])
            totalNetAmount = BankEntry.objects.filter(Date__range=[fromdate,todate],Person_Type="customer",Name=i['Name'],InvoiceId=i['InvoiceId']).order_by('-id').aggregate(Sum('Net_Balance_Paid')).get('Net_Balance_Paid__sum') or 0
            totalGSTAmount = BankEntry.objects.filter(Date__range=[fromdate,todate],Person_Type="customer",Name=i['Name'],InvoiceId=i['InvoiceId']).order_by('-id').aggregate(Sum('GST_Balance_Paid')).get('GST_Balance_Paid__sum') or 0
            entries_trans_amount = totalNetAmount + totalGSTAmount
            net_balance = total_debitors_amount - entries_trans_amount
            sundry_debitors_obj.append({ 
            'name' : i['Name'],
            'address' : f'{invoice[0].saleid.customer.customerid.Company_Address}, {invoice[0].saleid.customer.customerid.Company_City}-{invoice[0].saleid.customer.customerid.Company_Zip}, {invoice[0].saleid.customer.customerid.Company_State}, {invoice[0].saleid.customer.customerid.Company_Country}',
            'invoice_details' : invoice,
            'total' : total_debitors_amount,
            'net_balance' : net_balance,
            })
            Total_debitors_balance += net_balance
            debitors_total += total_debitors_amount

        
        context['active_agency'] = active_agency
        context['expences'] = expencesobj
        context['direct_expences'] = direct_expencesobj
        context['sales'] = salesobj
        context['purchase'] = purchaseobj
        context['total_expences'] = Expences.objects.filter(Agency=active_agency,Date__range=[fromdate,todate], Payment_Type='In Direct').aggregate(Sum('Amount'))
        context['total_direct_expences'] = Expences.objects.filter(Agency=active_agency,Date__range=[fromdate,todate], Payment_Type='Direct').aggregate(Sum('Amount'))
        context['total_sales'] = SalesInvoice.objects.filter(saleid__orderid__Agency=active_agency,Date__range=[fromdate,todate]).aggregate(Sum('saleid__sales__netAmount__WithGSTNetTotalAmount'))
        context['total_purchase'] = VoucherDetail.objects.filter(quotation__agency=active_agency,Date__range=[fromdate,todate]).aggregate(Sum('amount__total_amount'))
        # Sundry creditors
        context['Total_creditors_balance'] = Total_creditors_balance
        context['creditors_total'] = creditors_total
        context['sundry_creditors_obj'] = sundry_creditors_obj
        # Sundry debitors
        context['Total_debitors_balance'] = Total_debitors_balance
        context['debitors_total'] = debitors_total
        context['sundry_debitors_obj'] = sundry_debitors_obj

    return render(request, 'it-details/itdetails.html',context)

def ExpenceLedger(request, expcategory, fromdate, todate):
    particular_expence = serializers.serialize(
        'json',
        Expences.objects.filter(Date__range=[fromdate,todate],Payment_Type='In Direct',Expence_Category__Category=expcategory), 
        use_natural_foreign_keys=True,
        fields = ('Expence_Category','Amount','Payment_Mode','Date')
    )
    return HttpResponse(particular_expence)

def DirectExpenceLedger(request, expcategory, fromdate, todate):
    particular_direct_expence = serializers.serialize(
        'json',
        Expences.objects.filter(Date__range=[fromdate,todate],Payment_Type='Direct',Expence_Category__Category=expcategory), 
        use_natural_foreign_keys=True,
        fields = ('Expence_Category','Amount','Payment_Mode','Date')
    )
    return HttpResponse(particular_direct_expence)

def SalesLedger(request, month):
    custom_serializers = CustomSerializer()
    queryset = SalesInvoice.objects.filter(Date__month=month)
    particular_sales = custom_serializers.serialize(queryset,
    use_natural_foreign_keys=True, 
    fields=('Date','saleid','invoice','saleid__orderid__Sales_Company__Company_Name'))
    queryset1 = list(SalesInvoice.objects.filter(Date__month=month).values_list('saleid__sales'))
    print(queryset1)
    return HttpResponse(particular_sales)

def PurchaseLedger(request, month):
    custom_serializers = CustomSerializer()
    queryset = VoucherDetail.objects.filter(Date__month=month)
    particular_purchase = custom_serializers.serialize(queryset,
    use_natural_foreign_keys=True, 
    fields=('Date','amount','vendorDetail__Name'))
        
    return HttpResponse(particular_purchase)

def SundryCreditorsLedger(request, persontype, name, voucherid, fromdate, todate):
    active_agency = Agency.objects.all().filter(Active=True).first()

    particular_creditors = serializers.serialize(
        'json',
        BankEntry.objects.filter(agency=active_agency,Date__range=[fromdate,todate],Person_Type=persontype,Name=name,voucherId=voucherid).order_by('-id'),
        fields = ('Name','Post_Date','Value_Date','Total_Amount','Net_Balance_Paid','GST_Balance_Paid','Payment_Mode')
    )
    
    return HttpResponse(particular_creditors)

def SundryDebitorsLedger(request, persontype, name, invoiceid, fromdate, todate):
    active_agency = Agency.objects.all().filter(Active=True).first()

    particular_creditors = serializers.serialize(
        'json',
        BankEntry.objects.filter(agency=active_agency,Date__range=[fromdate,todate],Person_Type=persontype,Name=name,InvoiceId=invoiceid).order_by('-id'),
        fields = ('Name','Post_Date','Value_Date','Total_Amount','Net_Balance_Paid','GST_Balance_Paid','Payment_Mode')
    )
    
    return HttpResponse(particular_creditors)