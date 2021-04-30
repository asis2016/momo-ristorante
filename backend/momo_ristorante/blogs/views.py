"""
    blogs/views.py
    --------------
"""

from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from .forms import BlogForm
from .models import Blog


class BlogDetailView(DetailView):
    """ Return a detail of blog for administration. """
    model = Blog
    template_name = 'blogs/detail.html'


class BlogListView(ListView):
    """ Return a list of blog for administration. """
    model = Blog
    template_name = 'blogs/lists.html'
    context_object_name = 'blog_posts'


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
