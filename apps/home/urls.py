from django.urls import path
from apps.home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('phonebook', views.phonebooks, name="phonebooks"),
    path('gst-detail', views.gst_details, name="gst_details"),
    path('business-reports', views.businessReport, name="businessReport"),
    path('file-management', views.FileManagement, name="filemanagement"),
    path('balance-conformation-letter', views.BalanceConformationLetter, name="bcl"),
    path('dashboard-details', views.DashboardDetails, name="dashboard-details"),
    path('folders', views.path_to_dict, name="path_to_dict"),
    path('create-folder/<name>/<path>', views.createFolder, name="create-folder"),
    path('upload-file', views.uploadFile, name="upload-file"),
    path('path-files/<folder_name>', views.folder_path_files),
    path('delete-file/<path>', views.DeleteFile),
    path('settings', views.Settings, name="settings"),
    path('notifications-count', views.NotificationsCount, name="nitificount"),
]  