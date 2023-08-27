from django.urls import path
from apps.quicknotes import views

urlpatterns = [
    path('', views.Quicknotes, name='quicknotes'),
]