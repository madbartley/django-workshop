from django.shortcuts import render
from .models import Blog

# Create your views here.

def blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog_post.html', {'blog': blog})