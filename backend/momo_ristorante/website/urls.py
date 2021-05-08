import debug_toolbar
from django.urls import path, include

from . import views

urlpatterns = [

    # blogs
    path('blog', include('blogs.urls')),

    path('', views.home, name="home"),
    path('about/', views.AboutView.as_view(), name='about'),

    path('contact.html', views.contact, name='contact'),
    path('recipe.html', views.recipe, name='recipe'),
    path('recipe/<int:id>', views.recipe_detail, name='recipe_detail'),
    path('our-story.html', views.story, name='story'),
    path('reference.html', views.reference, name='references'),
    path('under-construction.html', views.underconstruction, name="under_construction"),

    path('__debug__/', include(debug_toolbar.urls)),

]
