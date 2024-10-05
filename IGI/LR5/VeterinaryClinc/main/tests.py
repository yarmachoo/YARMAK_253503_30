from django.test import TestCase
from django.urls import reverse


class MainModelTest(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

