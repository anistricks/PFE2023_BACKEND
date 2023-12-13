from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Article

class ArticleTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.article_data = {'nom': 'test'}
        self.article = Article.objects.create(nom='Test Article')

    def test_get_article_list(self):
        url = reverse('article-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_article(self):
        url = reverse('article-list')
        response = self.client.post(url, self.article_data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_article_detail(self):
        url = reverse('article-detail', args=[self.article.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_article(self):
        url = reverse('article-detail', args=[self.article.id])
        updated_data = {'nom': 'Updated Article'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Article.objects.get(id=self.article.id).nom, 'Updated Article')

    def test_delete_article(self):
        url = reverse('article-detail', args=[self.article.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Article.objects.filter(id=self.article.id).exists())
