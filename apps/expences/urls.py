from django.urls import path
from apps.expences import views

urlpatterns = [
    path('', views.ExpencesView, name="expences"),
]