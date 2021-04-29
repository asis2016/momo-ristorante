"""
    recipes/views.py
    ----------------
"""
from django.shortcuts import render
from django.views.generic import ListView

from .models import Recipe


class RecipeListView(ListView):
    """ Recipe ListView class. """
    model = Recipe
    template_name = 'recipes/recipe_list.html'


def list(request):
    """ Return render for recipe list. """
    recipe_list = Recipe.objects.all()
    return render(request, 'recipes/list.html', {
        'recipe_list': recipe_list
    })
