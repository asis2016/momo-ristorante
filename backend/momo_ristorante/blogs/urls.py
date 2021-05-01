from django.urls import path

from . import views

"""
    r'^([0-9]+)/$'	[0-9]+ - will match any number
                    () - will capture the value
"""
urlpatterns = [
    path('create.html', views.create, name='admin_url_blog_create'),
]
