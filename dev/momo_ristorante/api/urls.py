from django.urls import path

from . import views

urlpatterns = [
    # blog
    path('blogs/', views.ListBlog.as_view()),
    path('blogs/<int:pk>/', views.DetailBlog.as_view()),

    # recipes
    path('recipes/<int:pk>/', views.DetailRecipe.as_view()),
    path('recipes/', views.ListRecipe.as_view())
]
