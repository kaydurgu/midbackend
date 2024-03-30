from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from .views import WomenAPIList
from .models import Women
from rest_framework.test import APIClient

#client = APIClient()
#client.post('/notes/', {'title': 'new idea'}, format='json')
class WomenTestCase(APITestCase):
    def test_women(self):
        response = self.client.get(reverse('womenlist'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
class WomenListTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view =  WomenAPIList.as_view()
        self.url = reverse('womenlist')
    def test_women_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
       # self.assertEqual(response.data['count'], 0)
       # self.assertEqual(response.data['results'], [])

#class WomenAPI(APITestCase):
#    def test_create_account(self):
#        url = reverse('Women')
#        data = {'name': 'DabApps'}
#        response = self.client.post(url, data, format='json')
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#        self.assertEqual(Women.objects.count(), 1)
#        self.assertEqual(Women.objects.get().name, 'DabApps')