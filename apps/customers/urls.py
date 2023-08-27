from django.urls import path
from apps.customers import views

urlpatterns = [
    path('', views.Customers, name="customer"),
    path('add-customer', views.Add_Customer, name="add-customer"),
    path('update-customer/<pk>', views.Update_Customer, name="update-customer")
]