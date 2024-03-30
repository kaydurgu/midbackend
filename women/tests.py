from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from .views import WomenAPIList
from .models import Women
from rest_framework.test import APIClient

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

class WomenExceptionHandlingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invalid_data = {
        }

    def test_invalid_data_create(self):
        response = self.client.post('/womendetailed/3/', self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_nonexistent_object_retrieve(self):
        response = self.client.get('/womendetailed/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_nonexistent_object_update(self):
        response = self.client.put('/womendetailed/43/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_nonexistent_object_partial_update(self):
        response = self.client.patch('/womendetailed/2/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_nonexistent_object_delete(self):
        response = self.client.delete('/womendetailed/423/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



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

