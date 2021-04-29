from django.urls import path

from . import views

urlpatterns = [
    path('lists.html', views.lists, name='admin_url_employees'),
    path('index', views.index),
    path('create', views.create),
]
