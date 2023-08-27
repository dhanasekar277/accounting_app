from django.urls import path
from apps.orders import views

urlpatterns = [
    path('', views.Orders, name="orders"),
    path('add-order', views.AddOrder, name="add-order"),
    path('<id>', views.PurchaseOrder, name="purchase-order"),
    path('edit-order/', views.EditOrder, name="edit-order")
] 