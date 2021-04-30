"""
    api/views.py
    ------------
"""
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets

from blogs.models import Blog
from bookings.models import Booking
from recipes.models import Recipe
from .permissions import IsAuthorOrReadOnly
from .serializers import BlogSerializer, BookingSerializer, RecipeSerializer, UserSerializer


# Blog
class BlogDetail(generics.RetrieveAPIView):
    """ A single blog post as Retrieve API View. """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogList(generics.ListAPIView):
    """ List blog posts as List API View. """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# Booking
class DetailBooking(generics.RetrieveUpdateDestroyAPIView):
    """ A single booking as Retrieve Update Destroy API View. """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ListBooking(generics.ListCreateAPIView):
    """ List bookings as List Create API View. """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# Recipe
# todo refactor the name to RecipeList and RecipeDetail
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
    List of recipes as List Create API view.
    Option: ListAPIView or ListCreateAPIView
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    """
    User view set: combining "UserList and UserDetail."
    See: _views.old.py -> UserList and User Detail for "separate views."
    """
    # permission_classes = (IsAuthorOrReadOnly,) -> Note the difference.
    # permission_classes = ()
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
