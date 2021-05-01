"""
    recipes/views.py
    ----------------
"""
from django.views.generic import ListView

from .models import Recipe


class RecipeListView(ListView):
    """ Recipe ListView class. """
    model = Recipe
    template_name = 'recipes/lists.html'
    context_object_name = 'recipes'
