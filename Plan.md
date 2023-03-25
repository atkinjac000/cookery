# Cookery

A simple dinner idea picker using Django and the Spoontastic API.

## Requirements

- Display a list of recipes at the index.
- Have a pick button that sends you to the detail view for one of them.
- Pick a random dinner either from a database of the user's own recipes or from
the api.
- Save recipes to the database and get them out.
- Fetch recipes from the API?

## Models

**Recipe:**
- name
- instructions : String

**Ingredient**
- name
- recipe : many-to-many

## View Functions

- index : Returns the HTML for the recipe list
- new_recipe : Returns HTML for the form to put in a new recipe
- recipe_detail : Returns HTML for the details of a specific recipe

