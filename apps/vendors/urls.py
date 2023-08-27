from django.urls import path
from apps.vendors import views

urlpatterns = [
    path('', views.Vendors, name="vendors"),
    path('add-vendor/', views.Add_Vendor, name="add-vendor"),
    path('update-vendor/<pk>', views.Update_Vendor, name="update-vendor")
]