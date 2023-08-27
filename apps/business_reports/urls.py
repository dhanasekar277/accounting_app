from django.urls import path
from apps.business_reports import views

urlpatterns = [
    path('', views.customerSalesReports, name='sales_reports'),
    path('<int:pk>', views.customerSalesReports, name='sales_report'),
    path('purchase-reports', views.vendorPurchaseReports, name='purchase_reports'),
    path('purchase-reports/<int:pk>', views.vendorPurchaseReports, name='purchase_reports'),
    path('customers-reports', views.customersReports, name='customers_reports'),
    path('vendors-reports', views.vendorsReports, name='vendors_reports'),
]