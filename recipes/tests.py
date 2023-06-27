from django.contrib.auth.models import User
from .models import Recipe
from rest_framework import status
from rest_framework.test import APITestCase


class RecipeListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_recipess(self):
        adam = User.objects.get(username='adam')
        Recipe.objects.create(owner=adam, title='a title')
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_recipes(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/recipes/', {'title': 'a title', 'ingredients': 'Some ingredients', 'instructions': 'Some instructions'})
        count = Recipe.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_recipe(self):
        response = self.client.post('/recipes/', {'title': 'a title', 'ingredients': 'Some ingredients', 'instructions': 'Some instructions'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)