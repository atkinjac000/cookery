from django.shortcuts import render, get_object_or_404
from .models import Recipe

def index(request):
    recipes = Recipe.objects.all()

    return render(request, "dinner/index.html", {"recipes": recipes})

def new_recipe(request):
    name = ""
    return render(request, "dinner/new_recipe.html")


def recipe_detail(request, recipe_id):
    recipe_info = get_object_or_404(Recipe, pk=recipe_id)

    return render(request, "dinner/recipe_detail.html", {"recipe": recipe_info})

