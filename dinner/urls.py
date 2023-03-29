from django.urls import path
from . import views

app_name = "dinner"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:recipe_id>", views.recipe_detail, name="detail"),
    path("new", views.new_recipe, name="new_recipe"),
    path("create", views.create_recipe, name="create_recipe"),
    path("random", views.random_id, name="random_recipe"),
    path("ingredients", views.get_ingredients, name="ingredients"),
]
