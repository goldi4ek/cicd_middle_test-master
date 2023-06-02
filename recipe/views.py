from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category
from datetime import date
import random


def main(request):
    context = {
        "recipes": Recipe.objects.filter(created_at__year=2023)
    }
    return render(request, 'main.html', context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category_recipes = Recipe.objects.filter(category=category)
    return render(request, 'category_detail.html', {'recipes': category_recipes, 'category': category})