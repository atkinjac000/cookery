from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Recipe
from random import randint

def index(request):
    recipes = Recipe.objects.all()

    return render(request, "dinner/index.html", {"recipes": recipes})

def new_recipe(request):
    name = ""
    return render(request, "dinner/new_recipe.html")


def recipe_detail(request, recipe_id):
    recipe_info = get_object_or_404(Recipe, pk=recipe_id)

    return render(request, "dinner/recipe_detail.html", {"recipe": recipe_info})

def create_recipe(request):
    try:
        name = request.POST['recipe_name']
        instructions = request.POST['recipe_instructions']
    except(KeyError):
        return HttpResponseRedirect(reverse('dinner:index'))
    else:
        recipe = Recipe(name=name, instructions=instructions)
        recipe.save()
    return HttpResponseRedirect(reverse('dinner:index'))

def random_id(request):
    recipes = Recipe.objects.all()
    random_recipe = randint(0, len(recipes) - 1)
    return HttpResponseRedirect(reverse('dinner:detail', args=[recipes[random_recipe].id]))
