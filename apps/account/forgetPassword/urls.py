from django.urls import path
from apps.account.forgetPassword import views

urlpatterns = [
    path('', views.ForgetPassword, name="forgetpassword"),
]