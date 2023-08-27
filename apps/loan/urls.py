from django.urls import path
from apps.loan import views

urlpatterns = [
    path('', views.Loan, name="loan"),
]