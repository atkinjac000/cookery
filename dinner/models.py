from django.db import models

class Recipe(models.Model):
    name = models.charField(length=200)
    instructions = models.charField(length=5000)

class Ingredient(models.Model):
    name = models.charField(length=200)
    recipe = models.ManyToManyField(Recipe)

