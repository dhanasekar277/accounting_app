from django.urls import path
from apps.sales import views

urlpatterns = [
    path('', views.SaleView, name='sales'),
    path('sales-entry/<pk>', views.SalesEntry, name="sales-entry"),
    path('sales-view/<pk>', views.SalesView, name="sales-view"),
    path('sale-material/<int:pk>', views.GetSaleMaterial, name="sale-material")
    # path('sales-invoice-add', views.SalesInvoiceAdd, name="sales-invoice-add"),
]