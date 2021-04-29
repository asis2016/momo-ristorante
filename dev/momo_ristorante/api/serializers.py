"""
    api/serializers.py
    __________________
"""

from rest_framework import serializers

from blogs.models import Blog
from recipes.models import Recipe


class BlogSerializer(serializers.ModelSerializer):
    """ Blog model serializers. """

    class Meta:
        model = Blog
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    """ Recipe model serializers. """

    class Meta:
        model = Recipe
        fields = '__all__'
