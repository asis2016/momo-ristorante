"""
    blogs/views.py
    --------------
"""

from django.shortcuts import render, redirect

from .forms import BlogForm


def blogs(request):
    return render(request, 'blogs/blogs.html')


def create(request):
    """ create a new blog. """
    form = BlogForm(request.POST)
    if request.method == 'POST':
        form.save()
        return redirect('dashboard')
    else:
        form = BlogForm()
    return render(request, 'blogs/form.html', {'form': BlogForm})
