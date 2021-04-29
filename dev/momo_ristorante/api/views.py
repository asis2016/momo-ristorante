"""
    api/views.py
    ------------
"""
from rest_framework import generics, permissions

from blogs.models import Blog
from recipes.models import Recipe
from .permissions import IsAuthorOrReadOnly
from .serializers import BlogSerializer, RecipeSerializer


class DetailBlog(generics.RetrieveAPIView):
    """ A single blog post as Retrieve API View. """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class ListBlog(generics.ListAPIView):
    """ List or blog posts as List API View. """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class DetailRecipe(generics.RetrieveUpdateDestroyAPIView):
    """
    A single recipe as Retrieve Update Destroy API View.
    Options: RetrieveAPIView or RetrieveUpdateDestroyAPIView
    """
    permission_classes = (IsAuthorOrReadOnly, permissions.IsAuthenticated,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class ListRecipe(generics.ListCreateAPIView):
    """
    List of recipes as List Createve API view.
    Option: ListAPIView or ListCreateAPIView
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
