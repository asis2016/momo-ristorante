"""
    api/serializers.py
    __________________
"""

from rest_framework import serializers

from blogs.models import Blog
from bookings.models import Booking
from recipes.models import Recipe


class BlogSerializer(serializers.ModelSerializer):
    """ Blog model serializers. """

    class Meta:
        model = Blog
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """ Booking model serializiers. """

    class Meta:
        model = Booking
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    """ Recipe model serializers. """

    class Meta:
        model = Recipe
        fields = '__all__'
