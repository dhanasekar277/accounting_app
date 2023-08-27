from django.contrib import admin
from apps.quicknotes import models

# Register your models here.
class QuickNotesAdmin(admin.ModelAdmin):
    list_display = ['notes', 'published']

admin.site.register(models.Quicknotes, QuickNotesAdmin)