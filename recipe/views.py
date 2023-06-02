from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category


def main(request):
    context = {
        "recipes": Recipe.objects.filter(created_at__year=2023)
    }
    return render(request, 'main.html', context)


def recipe_detail(request, pk):
    context = {
        "recipe": Recipe.objects.get(pk=pk)
    }
    return render(request, 'recipe_detail.html', context)