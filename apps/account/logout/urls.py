from django.urls import path
from apps.account.logout import views

urlpatterns = [
    path('', views.Logout, name="logout")
]