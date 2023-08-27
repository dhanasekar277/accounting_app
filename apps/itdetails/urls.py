from django.urls import path
from . import views
from datetime import date

curyear = date.today().year

urlpatterns = [ 
    path('', views.ItDetails, name="it-details"),
    path('expence-ledger/<str:expcategory>/<str:fromdate>/<str:todate>', views.ExpenceLedger, name="expenceledger"),
    path('direct-expence-ledger/<str:expcategory>/<str:fromdate>/<str:todate>', views.DirectExpenceLedger, name="expenceledger"),
    path('sales-ledger/<int:month>', views.SalesLedger, name="salesledger"),
    path('purchase-ledger/<int:month>', views.PurchaseLedger, name="PurchaseLedger"),
    path('creditors-ledger/<str:persontype>/<str:name>/<int:voucherid>/<str:fromdate>/<str:todate>', views.SundryCreditorsLedger, name="sundrycreditorsledger"),
    path('debitors-ledger/<str:persontype>/<str:name>/<int:invoiceid>/<str:fromdate>/<str:todate>', views.SundryDebitorsLedger, name="Sundrydebitorsledger"),

]