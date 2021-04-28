"""momo_ristorante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
    Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from website.views import home, underconstruction, reference
from blogs.views import blogs, create

urlpatterns = [
    path('admin/', admin.site.urls),

    # static
    path('website/reference.html', reference, name='references'),
    path('under-construction.html', underconstruction, name="under_construction"),

    # dashboard
    path('website/', include('website.urls')),
    path('', home, name='home'),
    path('dashboard/', include('dashboard.urls')),
    path('employees/', include('employees.urls')),
    path('recipes/', include('recipes.urls')),

    #blog
    path('dashboard/blogs.html', blogs, name="blogs"),
    path('dashboard/blogs/create.html', create, name='blog_create')
]
