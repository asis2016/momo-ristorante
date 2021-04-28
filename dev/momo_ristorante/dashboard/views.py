from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):

    menus = ['dashboard_blog']
    return render(request, 'dashboard/index.html', {
        'menus': menus
    })

@login_required
def blog(request):
    return render(request, 'blogs/yo.html')

