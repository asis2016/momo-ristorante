from django.urls import path
from django.conf.urls import url

from . import views

"""
    r'^([0-9]+)/$'	[0-9]+ - will match any number
                    () - will capture the value
"""
urlpatterns = [
    path('lists.html', views.lists, name='admin_url_blog'),
    path('create.html', views.create, name='admin_url_blog_create'),
    path('detail.html', views.detail, name='admin_url_blog_detail'),
    url(r'^([0-9]+)/$', views.detail),
]


