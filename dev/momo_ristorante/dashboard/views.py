from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

menus = [
    {'title': 'Dashboard', 'url': 'admin_url_dashboard'},
    {'title': 'Blog', 'url': 'admin_url_blog'},
    {'title': 'Create a blog post', 'url': 'admin_url_blog_create'},
    {'title': 'Employees', 'url': 'admin_url_employees'},
    {'title': 'Site', 'url': 'home'},
]


@login_required
def index(request):
    """ Return localhost/dasbhoard """
    return render(request, 'dashboard/index.html', {
        'menus': menus,
        'SITE_NAME': settings.SITE_NAME
    })


@login_required
def blog(request):
    return render(request, 'blogs/yo.html')


def endpoints(request):
    """ REST API endpoints documentation. """
    endpoints = [
        '/api/v1/blogs',
        '/api/v1/blogs/1',
        '/api/v1/bookings',
        '/api/v1/bookings/1',
        '/api/v1/recipes',
        '/api/v1/recipes/1',
    ]
    return render(request, 'dashboard/endpoints/endpoints.html', {'endpoints': endpoints})
