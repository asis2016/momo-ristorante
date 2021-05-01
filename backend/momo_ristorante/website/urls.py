from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name='about'),
    path('blog.html', views.blogs, name='blog'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('contact.html', views.contact, name='contact'),
    path('recipe.html', views.recipe, name='recipe'),
    path('recipe/<int:id>', views.recipe_detail, name='recipe_detail'),
    path('our-story.html', views.story, name='story'),
    path('reference.html', views.reference, name='references'),
    path('under-construction.html', views.underconstruction, name="under_construction"),

]
