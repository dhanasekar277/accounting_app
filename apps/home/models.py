from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TYPE_CHOICES = (
    ('A', 'Add'),
    ('E', 'Edit'),
    ('D', 'Delete'),
)

class Notification(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Notifications = models.TextField()
    Status = models.BooleanField(default=True)
    Change = models.BooleanField(default=False)
    Types = models.CharField(max_length=1, choices=TYPE_CHOICES)
    doc = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.Notifications)



class Attendance(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Punch_In_Time =  models.DateTimeField(auto_now=True)
    Punch_Out_Time = models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return '{0}'.format(self.User)

class FileManagement(models.Model):
    File = models.FileField(upload_to='files')
    timestamp = models.DateTimeField(auto_now_add=True)
