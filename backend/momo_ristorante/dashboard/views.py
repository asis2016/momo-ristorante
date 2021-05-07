from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

menus = [
    {'title': 'Dashboard', 'url': 'admin_url_dashboard'},
    {'title': 'Blog', 'url': 'admin_blog'},
    {'title': 'Create a blog post', 'url': 'admin_url_blog_create'},
    {'title': 'Employees', 'url': 'admin_url_employees'},
    {'title': 'Site', 'url': 'home'},
]

from bookings.models import Booking
from blogs.models import Blog
from recipes.models import Recipe


def quick_stat():
    booking_count = Booking.objects.all().count()
    blog_post_count = Blog.objects.all().count()
    recipe_count = Recipe.objects.all().count()
    user_count = get_user_model().objects.all().count()

    quick_stats = [
        [blog_post_count, 'All posts', 'admin_blog'],
        [booking_count, 'All bookings', 'admin_bookings'],
        [recipe_count, 'All recipes', 'admin_recipes'],
        # todo refactor
        [user_count, 'All users', 'admin_url_dashboard']
    ]
    return quick_stats


@login_required
def index(request):
    """ Return localhost/dasbhoard """

    # quick stats about all models.

    return render(request, 'dashboard/index.html', {
        'menus': menus,
        'SITE_NAME': settings.SITE_NAME,
        'quick_stats': quick_stat()
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
