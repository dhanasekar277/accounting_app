
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.cash_format,name='cash_format'),
    # purchase 
    path('add_purchase_entry_form',views.add_purchase_entry_form,name='add_purchase_entry_form'),
    path('purchase_material_add/<int:id>',views.purchase_material_add,name='purchase_material_add'),
    path('edit_purchase_entry_form/<int:id>',views.edit_purchase_entry_form,name='edit_purchase_entry_form'),
    path('delete_purchase_entry/<int:id>',views.delete_purchase_entry,name='delete_purchase_entry'),
    path('delete_purchase_materials/<int:id>',views.delete_purchase_materials,name='delete_purchase_materials'),
    path('purchaseapi/<int:id>',views.purchaseapi,name='purchaseapi'),

    # sales
    path('add_sale_entry_form',views.add_sale_entry_form,name='add_sale_entry_form'),
    path('edit_sale_entry_form/<int:id>',views.edit_sale_entry_form,name='edit_sale_entry_form'),
    path('sales_material_add/<int:id>',views.sales_material_add,name='sales_material_add'),
    path('delete_sale_entry/<int:id>',views.delete_sale_entry,name='delete_sale_entry'),
    path('delete_sales_materials/<int:id>',views.delete_sales_materials,name='delete_sales_materials'),
    path('salesapi/<int:id>',views.salesapi,name='salesapi')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)