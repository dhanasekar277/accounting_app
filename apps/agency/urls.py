from django.urls import path
from apps.agency import views

urlpatterns = [
    path('', views.Agencies, name='agency'),
    path('add-agency', views.Add_Agency, name='add-agency'),
    path('update-agency/<pk>', views.Update_Agency, name='update-agency'),    
    path('update-agencies/<pk>', views.updateagency, name="update-agencies")
]