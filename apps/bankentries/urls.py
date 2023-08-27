from django.urls import path
from apps.bankentries import views

urlpatterns = [
    path('', views.BankEntries, name='bank_entries'),
    path('bank-entry-view/<str:type>/<int:id>', views.bankentryView,),
]