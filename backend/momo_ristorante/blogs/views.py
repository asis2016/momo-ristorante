"""
    blogs/views.py
    --------------
"""
from django.shortcuts import get_object_or_404, render

from .models import Blog


def blogs(request):
    """ Return blog archive. """
    blog_posts = Blog.objects.all()
    return render(request, 'blogs/index.html', {
        'blog_posts': blog_posts
    })


def blog_detail(request, id):
    """ Return single page for a blog. """
    blog_id = get_object_or_404(Blog, pk=id)
    return render(request, 'blogs/detail.html', {
        'blog': blog_id
    })
