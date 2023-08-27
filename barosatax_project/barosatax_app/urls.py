from django.urls import path, re_path
from . import views
from django.views.generic.base import RedirectView


favicon_view = RedirectView.as_view(url='./static/img/feviconlogo.jpg', permanent=True)

urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path('', views.home, name='home'),
    path('about-us', views.aboutus, name='aboutus'),

    path('services', views.services, name='services'),
    path('personal_tax', views.personal_tax, name='personal_tax'),
    path('corporate_tax', views.corporate_tax, name='corporate_tax'),
    path('self_employment', views.self_employment, name='self_employment'),
    path('business_incorporation', views.business_incorporation, name='business_incorporation'),
    path('business_advisory', views.business_advisory, name='business_advisory'),
    path('additional_corporation', views.additional_corporation, name='additional_corporation'),
    path('us_tax', views.us_tax, name='us_tax'),
    path('accounting_bookkeeping', views.accounting_bookkeeping, name='accounting_bookkeeping'),
    path('others', views.other_services, name='other_services'),

    path('customers', views.customers, name='customers'),
    path('locations', views.locations, name='locations'),
    path('blogs', views.blogs, name='blogs'),
    path('blog/<slug>', views.singel_blog, name='singel_blog'),
    path('contactus', views.contactus, name='contactus'),
]
