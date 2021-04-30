from django.urls import path
from . import views
from .views import RecipeListView

urlpatterns = [
    path('list.html', views.list),
    path('lists.html', RecipeListView.as_view(), name='admin_url_recipes')
]