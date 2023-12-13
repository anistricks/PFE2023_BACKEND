from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Client

class ClientTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.client_data = {'nom': 'Test', 'adresse_complete': '123 Test Street'}
        self.client_instance = Client.objects.create(nom='Existing Client', adresse_complete='456 Alma house')

    def test_get_client_list(self):
        url = reverse('client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_client(self):
        url = reverse('client-list')
        response = self.client.post(url, self.client_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_client_detail(self):
        url = reverse('client-detail', args=[self.client_instance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_client(self):
        url = reverse('client-detail', args=[self.client_instance.id])
        updated_data = {'nom': 'Updated Client', 'adresse_complete': '789 new address'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Client.objects.get(id=self.client_instance.id).nom, 'Updated Client')

    def test_delete_client(self):
        url = reverse('client-detail', args=[self.client_instance.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Client.objects.filter(id=self.client_instance.id).exists())

