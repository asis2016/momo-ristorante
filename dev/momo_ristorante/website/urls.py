from django.urls import path

from .views import home, blogs, blog_detail, recipe, recipe_detail, about

urlpatterns = [
    path('', home, name="home"),
    path('blog.html', blogs, name='blog'),
    path('blog/<int:id>', blog_detail, name='blog_detail'),

    path('recipe.html', recipe, name='recipe'),
    path('recipe/<int:id>', recipe_detail, name='recipe_detail'),

    path('about', about)

]
