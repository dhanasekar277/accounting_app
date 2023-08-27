from django.shortcuts import render
from .models import Blogs, Comments
import random


# Create your views here.
def home(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'about_us.html')


def services(request):
    return render(request, 'services.html')


def personal_tax(request):
    return render(request, 'service/personal_tax.html')


def corporate_tax(request):
    return render(request, 'service/corporate_tax.html')


def self_employment(request):
    return render(request, 'service/self_employment.html')


def business_incorporation(request):
    return render(request, 'service/business_incorporation.html')


def business_advisory(request):
    return render(request, 'service/business_advisory.html')


def additional_corporation(request):
    return render(request, 'service/additional_corporation.html')


def us_tax(request):
    return render(request, 'service/us_tax.html')


def accounting_bookkeeping(request):
    return render(request, 'service/accounting_bookkeeping.html')


def other_services(request):
    return render(request, 'service/others.html')


def customers(request):
    return render(request, 'customers.html')


def locations(request):
    return render(request, 'locations.html')


def blogs(request):
    context = {
        'blog': Blogs.objects.all()
    }
    return render(request, 'blogs.html', context)


def singel_blog(request, slug):
    blog_id = Blogs.objects.filter(slug=slug)
    bl_id = Blogs.objects.get(slug=slug)

    blog_view_count = bl_id.views + 1
    Blogs.objects.filter(slug=slug).update(views=blog_view_count)

    if request.method == 'POST':
        cmt_name = request.POST['cmt_name']
        cmt_email = request.POST['cmt_email']
        cmt_phn = request.POST['cmt_phone']
        cmt = request.POST['cmt_message']
        b_id = blog_id[0].id
        comment = Comments.objects.create(name=cmt_name, email=cmt_email, phone=cmt_phn, message=cmt)
        bl_id.comments.add(comment)
        bl_id.save()

    num_entities = Blogs.objects.all().count()
    rand_entities = random.sample(range(num_entities), 3)

    sample_entities = Blogs.objects.filter(id__in=rand_entities)
    context = {
        'blog': blog_id,
        'featured': sample_entities
    }
    return render(request, 'blog_view.html', context)


def contactus(request):
    return render(request, 'contactus.html')
