from django.urls import path
from django.conf.urls import url
from .views import index, blog
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('', index, name = 'dashboard' ),
    # or,
    # url(r'index$', index, name = 'dashboard_index' ),

    url(r'blog$', blog, name = 'dashboard_blog'),

    url(r'login$',
        LoginView.as_view(template_name = 'dashboard/login.html'),
        name = 'dashboard_login'
    ),

    url(r'logout$',
        LogoutView.as_view(),
        name = 'dashboard_logout'
    )
    
    #path('home.html', views.home),
    
]

