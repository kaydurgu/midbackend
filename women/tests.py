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
class WomenExceptionHandlingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invalid_data = {
            # Invalid data for testing error handling
        }

    def test_invalid_data_create(self):
        response = self.client.post('/your-api-endpoint/', self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_nonexistent_object_retrieve(self):
        response = self.client.get('/your-api-endpoint/999/')  # Assuming ID 999 doesn't exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_nonexistent_object_update(self):
        response = self.client.put('/your-api-endpoint/999/', {}, format='json')  # Assuming ID 999 doesn't exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_nonexistent_object_partial_update(self):
        response = self.client.patch('/your-api-endpoint/999/', {}, format='json')  # Assuming ID 999 doesn't exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_nonexistent_object_delete(self):
        response = self.client.delete('/your-api-endpoint/999/')  # Assuming ID 999 doesn't exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Add more tests for other exception handling scenarios as needed


class WomenDataValidationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_data = {
            "title": "Hanbolot",
            "cat_1": "2",
        }

    def test_valid_data_create(self):
        response = self.client.post('/womenlist/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_blank_field_create(self):
        invalid_data = self.valid_data.copy()
        invalid_data["cat_id"] = "1"  # Making a required field blank
        response = self.client.post('/womenlist/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unique_field_create(self):

        Women.objects.create(**self.valid_data)
        response = self.client.post('/womenlist/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#class WomenAPI(APITestCase):
#    def test_create_account(self):
#        url = reverse('Women')
#        data = {'name': 'DabApps'}
#        response = self.client.post(url, data, format='json')
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#        self.assertEqual(Women.objects.count(), 1)
#        self.assertEqual(Women.objects.get().name, 'DabApps')