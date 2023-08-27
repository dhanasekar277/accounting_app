from django.urls import path
from apps.products import views

urlpatterns = [
    path('', views.Products, name="products"),
    path('productviewapi/<str:name>', views.productViewApi)
]