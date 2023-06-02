from django.test import RequestFactory, Client
from django.urls import reverse
from .models import Recipe, Category
from django.test import TestCase
from django.contrib.auth.models import User


class RecipeAppTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category')

    def test_category_detail_view(self):
        # Test the category detail view
        response = self.client.get(reverse('category_detail', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')



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


class CategoryDetailViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category')
        self.url = reverse('category_detail', args=[self.category.id])

    def test_category_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'category_detail.html')

    def test_category_detail_view_category(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['category'], self.category)

    def test_category_detail_view_invalid_category_id(self):
        invalid_url = reverse('category_detail', args=[999])
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, 404)