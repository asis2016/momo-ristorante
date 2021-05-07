"""
    blogs/views.py
    --------------
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Blog


class BlogDetailView(LoginRequiredMixin, DetailView):
    """ Return a detail of blog for administration. """
    model = Blog
    template_name = 'blogs/detail.html'
    context_object_name = 'blog'


class BlogListView(LoginRequiredMixin, ListView):
    """ Return a list of blog for administration. """
    app_header = {
        'title': 'Blogs',
        'admin_url_blog_create': 'admin_url_blog_create'
    }
    model = Blog
    paginate_by = 4
    template_name = 'blogs/blog.html'
    context_object_name = 'blog_posts'
    extra_context = app_header


class BlogCreateView(LoginRequiredMixin, CreateView):
    """ Create a new blog post. """
    model = Blog
    template_name = 'blogs/new.html'
    fields = '__all__'


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """ Updtas an exisitng blog post. """
    model = Blog
    template_name = 'blogs/edit.html'
    context_object_name = 'blog_post'
    fields = ['title', 'excerpt', 'content', 'image']


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """ A single post delete. """
    model = Blog
    template_name = 'blogs/delete.html'
    context_object_name = 'blog_post'
    success_url = reverse_lazy('admin_blog')
