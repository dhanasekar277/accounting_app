from django.urls import path
from apps.invoice import views

urlpatterns = [
    path('sales-invoice/<pk>', views.Invoice, name="sales-invoice"),
    path('get-latest-invoice', views.GetLatestInvoice)
]
