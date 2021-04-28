"""
    website/views.py
    ================
    Main entry view for 'public'.
"""
__author__ = "Ashish Singh Maharjan"

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blogs.models import Blog
from recipes.models import Recipe
from .models import Homepage, Setting


def datas():
    """
    Returns data for home.
    Read the documentation for the :meth: `home` method.
    """
    data = {
        "blog": Blog.objects.all(),
        "recipes": Recipe.objects.all(),
        'featurette': Homepage.objects.get(pk='featurette'),
        "homepage": Homepage.objects.all(),
        "jumbotron": Homepage.objects.get(pk='jumbotron'),
        "setting": Setting.objects.get(pk=1),
    }
    return data


def home(request):
    """ Return render or HttpResponse for website > home. """
    if request.user.is_authenticated:
        return render(request, "website/index.html", datas())
    else:
        return HttpResponse('you are not authenticated!')


def reference(request):
    """ Return all external references used for the developing this project. """
    return render(request, 'references/reference.html', datas())


def underconstruction(request):
    """ Return "not developed" pages. """
    return render(request, 'under_construction/under_construction.html')


def blogs(request):
    """ Return blog archive. """
    blog_posts = Blog.objects.all()
    return render(request, 'website/blog.html', {
        'blog_posts': blog_posts
    })


def blog_detail(request, id):
    """
    Return single page for a blog.
    :param id: blog id
    :return: render()
    """
    blog_id = get_object_or_404(Blog, pk=id)
    return render(request, 'website/blog_detail.html', {
        'blog': blog_id
    })


def recipe(request):
    """ Return gallery arhive. """
    posts = Recipe.objects.all()
    return render(request, 'website/recipe.html', {
        'posts': posts
    })


def recipe_detail(request, id):
    """ Return single page for a gallery. """
    post = get_object_or_404(Recipe, pk=id)
    return render(request, 'website/recipe_detail.html', {
        'post': post
    })


def about(request):
    """ Return about page. """
    return HttpResponse('Yo this is about page.')

# def contact(request, id):
#    return HttpResponse('Yo this is contact page ' + str(id))
