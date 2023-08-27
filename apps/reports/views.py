from django.shortcuts import render
from apps.agency.models import Agency
from apps.vendors.models import Vendor
from apps.customers.models import Customer
from apps.products.models import Product
from apps.orders.models import Order
from apps.quotations.models import Quotation
from apps.purchase.models import SinglePurchaseEntry
from apps.voucher.models import VoucherDetail,Voucher
from apps.sales.models import Sales
from apps.invoice.models import SalesInvoice
from apps.expences.models import Expences
from apps.bankentries.models import BankEntry
from apps.loan.models import Loan

# Create your views here.


def reports(request):  
    print(SalesInvoice.objects.values_list('invoice__orderid__Materials__Product_Name__GST').first())
    context = {
        'gst' : SalesInvoice.objects.values_list('invoice__orderid__Materials__Product_Name__GST').first(),
    }
    if request.GET.get("from"):
        fromdate = request.GET.get("from")
        todate = request.GET.get("to")
        model = request.GET.get("model")

        reportsData = {
            "agency": Agency.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
            "vendor": Vendor.objects.filter(published__range=[fromdate, todate]).order_by('-id'),
            "customer": Customer.objects.filter(published__range=[fromdate, todate]).order_by('-id'),
            "product": Product.objects.filter(Timestamp__range=[fromdate, todate]).order_by('-id'),
            "order": Order.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
            "quotation": Quotation.objects.filter(published__range=[fromdate, todate]).order_by('-id'),
            "purchase": SinglePurchaseEntry.objects.filter(doc__range=[fromdate, todate]).order_by('-id'),
            "voucher": VoucherDetail.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
            "sales": Sales.objects.filter(doc__range=[fromdate, todate]).order_by('-id'),
            "invoice": SalesInvoice.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
            "expence_entries": Expences.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
            "bank_entries": BankEntry.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
            "net_purchase": Voucher.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
            "net_payable": Voucher.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
            "net_sales": SalesInvoice.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
            "net_reciveable": SalesInvoice.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
            "loan_management": Loan.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
            "purchase_gst_details": Voucher.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
            "sales_gst_details": SalesInvoice.objects.filter(Date__range=[fromdate, todate]).order_by('-id'),
        }[model]
        # print(reportsData)
        context['data'] = reportsData
        context['model'] = model

    return render(request, "reports/reports.html", context)


