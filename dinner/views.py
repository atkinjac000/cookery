from django.shortcuts import render
from .models import Recipe
def index(request):
    recipes = Recipe.objects.all()

    return render(request, "/dinner/index.html", {"recipes": recipes})
