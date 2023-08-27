from django.contrib import admin
from .models import Comments, Blogs, Testimonials

# Register your models here.
admin.site.register(Testimonials)

@admin.register(Comments)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_on')
    search_fields = ['name', 'email']

@admin.register(Blogs)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}



# Register your models here.
admin.site.site_header = "BarosaTax"
admin.site.site_title = "BarosaTax"
admin.site.index_title = "BarosaTax Administration"
admin.site.site_header = "BarosaTax"
admin.site.site_title = "BarosaTax"
admin.site.index_title = "BarosaTax Administration"