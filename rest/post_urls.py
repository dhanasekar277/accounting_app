from django.urls import path, include
from rest import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'agency', views.AgencyPostViewSet)
router.register(r'products', views.ProductWithOutViewSet)
router.register(r'vendors', views.VendorPostViewSet)
router.register(r'material-info', views.MaterialInfo_ViewSet)
router.register(r'orders', views.POSTOrderViewSet)
router.register(r'customers', views.CustomerPostViewSet)
router.register(r'quotations', views.QuotationViewSet)
router.register(r'quotation-detail', views.CusQuotationDetailViewSet)
router.register(r'quotation-term', views.CusQuotationTermsViewSet)
router.register(r'quotation-vendor-detail', views.VendorQuotationDetailViewSet)
router.register(r'notifications', views.NotificationWithOutInfoViewSet)
router.register(r'vendor-gst', views.POSTVendorGSTViewSet)
router.register(r'purchase-material-entry', views.PostPurchaseMaterialEntryViewSet)
router.register(r'purchase-remainder', views.PostPurchaseRemainderViewSet)
router.register(r'purchase-net-amount', views.PostPurchaseNetAmountViewSet)
router.register(r'purchase-info', views.PostPurchaseInvoiceViewSet)
router.register(r'single-purchase-entry', views.PostSinglePurchaseEntryViewSet)
router.register(r'purchase-entry', views.PostPurchaseEntryViewSet)
router.register(r'voucher-vendor-info', views.PostVoucherVendorInfoViewSet)
router.register(r'voucher-base-info', views.PostPurchaseBasicInfoViewSet)
router.register(r'voucher-amount', views.PostVourcherAmountViewSet)
router.register(r'voucher-detail', views.PostSingleVoucherViewSet)
router.register(r'voucher-signature', views.PostVoucherSignatureViewSet)
router.register(r'voucher', views.PostVouchersViewSet)
router.register(r'sales-customer', views.PostCutomerInfoViewSet)
router.register(r'sales', views.PostSalesViewSet)
router.register(r'sales-collection', views.PostSalesCollectionViewSet)
router.register(r'sales-material-info', views.PostSalesMaterialInfoViewSet)
router.register(r'sales-total', views.PostSalesTotalViewSet)
router.register(r'dc-detail', views.PostDCDetailViewSet)
router.register(r'single-invoice', views.PostSingleSalesInvoiceViewSet)
router.register(r'sale-invoice', views.PostSalesInvoiceViewSet)
router.register(r'bank-entries', views.PostBankEntryViewSet)
router.register(r'vendor-material-supplying', views.PostVendorMaterialSupplyingViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
