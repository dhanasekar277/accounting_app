from email.policy import default
from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User, Group
# Create your models here.


class Testimonials(models.Model):
    name = models.CharField(max_length=255, blank=True)
    quote = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Comments(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    description = QuillField()
    comments = models.ManyToManyField(Comments, blank=True)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created_on']
