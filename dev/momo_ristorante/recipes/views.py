from django.shortcuts import render
from .models import Recipe

def list(request):
    recipe_list = Recipe.objects.all()
    return render(request, 'recipes/list.html', {
        'recipe_list': recipe_list
    })
