"""
    website/views.py
    ================
    Main entry view for 'public'.
"""
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


def about(request):
    """ Return about page. """
    posts = [
        {'title': 'Flabio Gustava', 'image': 'about-3.png'},
        {'title': 'Maria Smith', 'image': 'about-2.png'},
        {'title': 'Johnny Harris', 'image': 'about-1.png'}
    ]
    return render(request, 'about/about.html', {'posts': posts})


def blogs(request):
    """ Return blog archive. """
    blog_posts = Blog.objects.all()
    return render(request, 'blogs/index.html', {
        'blog_posts': blog_posts
    })


def blog_detail(request, id):
    """
    Return single page for a blog.
    :param id: blog id
    :return: render()
    """
    blog_id = get_object_or_404(Blog, pk=id)
    return render(request, 'blogs/blog_detail.html', {
        'blog': blog_id
    })


def contact(request):
    """ Return a contact page. """
    return render(request, 'contact/contact.html')


def home(request):
    """ Return render or HttpResponse for website > home. """
    return render(request, "website/index.html", datas())


def my_account(request):
    """ todo my account page with quick stat. """
    if request.is_authenticated:
        return HttpResponse('Yo this is my account. Quick stat page.')
    else:
        return HttpResponse('You are not authorized.')


def recipe(request):
    """ Return gallery arhive. """
    posts = Recipe.objects.all()
    return render(request, 'recipes/recipe.html', {
        'posts': posts
    })


def recipe_detail(request, id):
    """ Return single page for a gallery. """
    recipe = get_object_or_404(Recipe, pk=id)
    return render(request, 'recipes/detail.html', {
        'recipe': recipe
    })


def reference(request):
    """ Return all external references used for the developing this project. """
    return render(request, 'references/reference.html', datas())


def story(request):
    """ Return Our story page. """
    return render(request, 'story/our-story.html')


def underconstruction(request):
    """ Return "not developed" pages. """
    return render(request, 'under_construction/under_construction.html')

# def contact(request, id):
#    return HttpResponse('Yo this is contact page ' + str(id))
