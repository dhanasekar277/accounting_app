from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # home url
    path('', include('apps.home.urls')),
    ### account url
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('logout/', include('apps.account.logout.urls')),
    path('forget-password/', include('apps.account.forgetPassword.urls')),
    # static data url
    path('agencies/', include('apps.agency.urls')),
    path('products/', include('apps.products.urls')),
    path('vendors/', include('apps.vendors.urls')),
    path('customers/', include('apps.customers.urls')),
    # orders app url
    path('orders/', include('apps.orders.urls')),
    path('purchase/', include('apps.purchase.urls')),
    path('bank-entries/', include('apps.bankentries.urls')),
    path('quicknotes/', include('apps.quicknotes.urls')),
    path('quotations/', include('apps.quotations.urls')),
    path('vouchers/', include('apps.voucher.urls')),
    path('invoices/', include('apps.invoice.urls')),
    path('expences/', include('apps.expences.urls')),
    path('balancesheet/', include('apps.balancesheet.urls')),
    path('it-details/', include('apps.itdetails.urls')),
    path('net-payment/', include('apps.netpayment.urls')),
    path('business-reports/', include('apps.business_reports.urls')),
    path('loan/', include('apps.loan.urls')),
    path('sales/', include('apps.sales.urls')),
    path('reports/', include('apps.reports.urls')),
    path('api/', include('rest.urls')),
    path('post-api/', include('rest.post_urls'))
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
