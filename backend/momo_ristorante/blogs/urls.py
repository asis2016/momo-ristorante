from django.urls import path
from django.conf.urls import url

from . import views

"""
    r'^([0-9]+)/$'	[0-9]+ - will match any number
                    () - will capture the value
"""
urlpatterns = [
    path('', views.BlogListView.as_view(), name='admin_url_blog'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='admin_url_blog_detail'),

    path('create.html', views.create, name='admin_url_blog_create'),
]


