from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from users.models import Client
from users.models import Doctor


class ClientModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            username="username",
            email="veroni.rmk@gmail.com",
            phone_number="+375445788672",
            date_birth=datetime.now(),
            first_name="first name",
            last_name="last name",
            address="Адрес"
        )

    def test_article_creation(self):
        self.assertTrue(isinstance(self.client, Client))
        self.assertEqual(str(self.client), self.client.last_name)

    def test_invalid_phone(self):
        self.client.phone_number = "12345"
        with self.assertRaises(ValidationError):
            self.client.full_clean()

    def test_invalid_email(self):
        self.client.email = "12345"
        with self.assertRaises(ValidationError):
            self.doctor.full_clean()

class DoctorModelTest(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            username="username",
            email="veroni.rmk@gmail.com",
            phone_number="+375445788672",
            date_birth=datetime.now(),
            first_name="first name",
            last_name="last name"
        )

    def test_article_creation(self):
        self.assertTrue(isinstance(self.doctor, Doctor))
        self.assertEqual(str(self.doctor), self.doctor.last_name)

    def test_invalid_phone(self):
        self.client.phone_number = "12345"
        with self.assertRaises(ValidationError):
            self.doctor.full_clean()

    def test_invalid_email(self):
        self.client.email = "12345"
        with self.assertRaises(ValidationError):
            self.doctor.full_clean()