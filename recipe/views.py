from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category
import random


def main(request):
    recipes = Recipe.objects.all()
    random_recipes = random.sample(list(recipes), 10)
    return render(request, 'main.html', {'recipes': random_recipes})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category_recipes = Recipe.objects.filter(category=category)
    return render(request, 'category_detail.html', {'recipes': category_recipes, 'category': category})