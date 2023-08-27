from django.contrib import admin
from apps.home.models import Notification, Attendance, FileManagement
# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['Notifications', 'Status', 'Change', 'Types']

admin.site.register(Notification, NotificationAdmin)


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['User', 'Punch_In_Time', 'Punch_Out_Time']

admin.site.register(Attendance, AttendanceAdmin)

admin.site.register(FileManagement)