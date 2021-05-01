"""
    api/views.py
    ------------
"""
from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets

from blogs.models import Blog
from bookings.models import Booking
from recipes.models import Recipe
from .permissions import IsAuthorOrReadOnly
from .serializers import BlogSerializer, BookingSerializer, RecipeSerializer, UserSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    Blog view set.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    Booking view set.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    Recipe view set: combining "UserList and UserDetail."
    """
    permission_classes = (IsAuthorOrReadOnly, permissions.IsAuthenticated,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User view set: combining "UserList and UserDetail."
    See: _views.old.py -> UserList and User Detail for "separate views."
    """
    # permission_classes = (IsAuthorOrReadOnly,) -> Note the difference.
    # permission_classes = ()
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
