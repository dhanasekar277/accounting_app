from django.urls import path
from apps.purchase import views
 
urlpatterns = [
    path('', views.Purchases, name="purchase"),
    path('view/<quotation>/<vendor>', views.PurchaseView, name="purchase-view"),
    path('invoice/<quotation>/<vendor>', views.PurchasesInvoice, name="purchase-invoice"),
    path('entries/<id>', views.PurchasesEntries, name="purchase-entries"),
    path('pm/<pk>', views.GetPurchaseMaterial, name="purchase-material"),
    path('purchase-voucher', views.PurchasesVoucher, name="purchase-voucher"),
    path('purchase-voucher-add', views.PurchasesVoucherAdd, name="purchase-voucher-add"),
    path('add-purchase', views.AddPurchase, name="add-purchase"),
] 