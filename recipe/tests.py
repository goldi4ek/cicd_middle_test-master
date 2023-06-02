from django.test import RequestFactory, Client
from django.urls import reverse
from .models import Recipe, Category
from django.test import TestCase
from django.contrib.auth.models import User


class RecipeAppTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category')

    def test_recipe_detail_view(self):
        recipe = Recipe.objects.create(title='Test Recipe', ingredients='Test Ingredient', category=self.category)
        response = self.client.get(reverse('recipe_detail', args=[recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')
        self.assertEqual(response.context['recipe'], recipe)


class MainViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.category = Category.objects.create(name='Main Course')
        self.recipes = [
            Recipe.objects.create(title='Recipe 1', ingredients='Ingredient 1', category=self.category),
            Recipe.objects.create(title='Recipe 2', ingredients='Ingredient 2', category=self.category),
            Recipe.objects.create(title='Recipe 3', ingredients='Ingredient 3', category=self.category),
            Recipe.objects.create(title='Recipe 4', ingredients='Ingredient 4', category=self.category),
            Recipe.objects.create(title='Recipe 5', ingredients='Ingredient 5', category=self.category),
        ]