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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'MOMO API'
API_DESCRIPTION = 'MOMO API documentation.'
schema_view = get_schema_view(title=API_TITLE)
schema_view_swagger = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),

    # account - login
    path('account/login.html', LoginView.as_view(template_name='accounts/login.html'), name='login'),

    # dashboard
    path('dashboard/', include('dashboard.urls')),

    # api
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),

    # docs
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),

    # schema
    path('schema/', schema_view),

    # schema-swagger
    path('swagger-docs/', schema_view_swagger),

    # website
    path('', include('website.urls'))
]

if settings.DEBUG:
    urlpatterns += [
        url(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
