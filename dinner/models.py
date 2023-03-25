from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    instructions = models.CharField(max_length=5000)

    class Meta:
        ordering = ['name']

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    recipe = models.ManyToManyField(Recipe)

    class Meta:
        ordering = ['name']

