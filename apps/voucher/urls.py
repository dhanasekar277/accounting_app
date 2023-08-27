from django.urls import path
from apps.voucher import views

urlpatterns = [
    path('voucher-count/<id>', views.GetVoucherCount, name='voucher-count'),
    path('view/<quotation>/<vendorId>', views.VoucherView, name='voucher-view')
]