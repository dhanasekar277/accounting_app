from .models import Testimonials

def get_testimonials(request):
    testimonials = Testimonials.objects.all()
    return dict(testimonials=testimonials)