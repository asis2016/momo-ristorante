"""
    blogs/views.py
    --------------
"""

from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import BlogForm
from .models import Blog


class BlogDetailView(DetailView):
    """ Return a detail of blog for administration. """
    model = Blog
    template_name = 'blogs/detail.html'
    context_object_name = 'blog'


class BlogListView(ListView):
    """ Return a list of blog for administration. """
    model = Blog
    template_name = 'blogs/blog.html'
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
    return render(request, 'blogs/new.html', {'form': BlogForm})


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blogs/edit.html'
    context_object_name = 'blog_post'
    fields = ['title','excerpt', 'content', 'image']


class BlogDeleteView(DeleteView):
    """ A single post delete. """
    model = Blog
    template_name = 'blogs/delete.html'
    context_object_name = 'blog_post'
    success_url = reverse_lazy('admin_blog')