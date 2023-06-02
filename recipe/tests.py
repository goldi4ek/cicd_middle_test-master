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


class ViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='testpass')
        self.category = Category.objects.create(name='Test Category')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='This is a test recipe.',
            instructions='Test instruction 1\nTest instruction 2',
            ingredients='Test ingredient 1\nTest ingredient 2',
            category=self.category,
        )

    def test_main_view(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')
        self.assertNotContains(response, 'Old Recipe')
        self.assertEqual(len(response.context['recipes']), 1)
class CategoryModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_str(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_iter(self):
        self.assertEqual(list(self.category), [])


class RecipeModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='This is a test recipe.',
            instructions='Test instruction 1\nTest instruction 2',
            ingredients='Test ingredient 1\nTest ingredient 2',
            category=self.category,
        )

    def test_str(self):
        self.assertEqual(str(self.recipe), 'Test Recipe')