# Cookery

A simple dinner idea picker using Django and the Spoontastic API.

## Requirements

- Pick a random dinner either from a database of the user's own recipes or from
the api.
  - Save recipes to the database.
  - Access database recipes.
  - Fetch recipes from the API.

## Models

**Recipe:**
- name
- ingredient : one-to-many
- instructions : String

**Ingredient**
- name

