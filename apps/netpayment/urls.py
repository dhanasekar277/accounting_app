from django.urls import path
from apps.netpayment import views

urlpatterns = [
        path('', views.NetPaymentPayable, name="netpay"),
        path('net-recivable', views.NetPaymentRecivable, name="netrecive"),
        path('net-purchase', views.NetPurchase, name="netpurchase"),
        path('net-sales', views.NetSales, name="netsales"),
        path('net-purchase-json', views.NetPurchaseJson, name="netpurjson"),
        path('net-sales-json', views.NetSalesJson, name="netsalesjson"),

]