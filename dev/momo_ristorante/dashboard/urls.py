from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [

    path('index.html', views.index, name='admin_url_dashboard'),
    # or,
    # url(r'index$', index, name = 'dashboard_index' ),

    url(r'blog$', views.blog, name='dashboard_blog'),

    url(r'login$',
        LoginView.as_view(template_name='dashboard/login.html'),
        name='dashboard_login'
        ),

    url(r'logout$',
        LogoutView.as_view(),
        name='dashboard_logout'
        ),

    # path('home.html', views.home),

    path('endpoints.html', views.endpoints, name='admin_url_endpoints')

]
