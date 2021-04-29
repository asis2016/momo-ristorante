"""
    blogs/views.py
    --------------
"""

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import BlogForm
from .models import Blog


def blogs(request):
    return render(request, 'blogs/blogs.html')


def create(request):
    """ create a new blog. """
    form = BlogForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
        return redirect('blog_lists_url')
    else:
        form = BlogForm()
    return render(request, 'blogs/form.html', {'form': BlogForm})


def lists(request):
    """ Return all blog. """
    #user = User.objects.get(username='root')
    blog_posts = Blog.objects.all()
    return render(request, 'blogs/lists.html', {'blog_posts': blog_posts})


def detail(request, blog_id):
    """
    Return a detail of blog for administration.
    :param request:
    :param blog_id:
    :return:
    """
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})
    # return HttpResponse('this is from blog detail'+blog_id)
