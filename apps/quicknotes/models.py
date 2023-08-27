from django.db import models

# Create your models here.

class Quicknotes(models.Model):
    notes = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.notes)
