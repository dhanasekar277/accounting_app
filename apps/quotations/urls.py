from django.urls import path
from apps.quotations import views

urlpatterns = [
    path('',views.Quotations,name='quotations'),
    path('add-quotation',views.AddQuotations,name='addquotation'),
]