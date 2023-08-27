from django.contrib import admin
from apps.products import models
# Register your models here.


""" Product Quality """
class ProductQualityAdmin(admin.ModelAdmin):
    list_display = ['Quality', 'Price']

admin.site.register(models.ProductQuality, ProductQualityAdmin)


""" Product Quality """
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Vendor', 'Product', 'GST', 'HSNCode', 'Ton']
    # list_editable = ['HSNCode']

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.LatestPrice)