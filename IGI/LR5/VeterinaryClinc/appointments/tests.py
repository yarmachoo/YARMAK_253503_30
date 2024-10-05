from datetime import timezone, timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from appointments.models import Order, Service
from clients.models import Pet
from users.models import Client, Doctor


class OrderViewsTest(TestCase):
    # Set up your test environment
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.doctor = Doctor.objects.create(user=self.user, name='Dr. Smith')
        self.client.force_login(self.user)

    def test_doctors_schedule_view(self):
        # Create some orders
        Order.objects.create(doctor=self.doctor, date=timezone.now() - timedelta(days=2))
        Order.objects.create(doctor=self.doctor, date=timezone.now())
        Order.objects.create(doctor=self.doctor, date=timezone.now() + timedelta(days=2))

        # Make GET request to the view
        response = self.client.get(reverse('doctors_schedule'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dr. Smith')

    def test_order_create_view_GET(self):
        # Make GET request to the view
        response = self.client.get(reverse('order_create'))
        self.assertEqual(response.status_code, 200)

    def test_order_create_view_POST(self):
        # Create necessary linked instances
        pet = Pet.objects.create(name='Rex', owner=self.user)
        service = Service.objects.create(name='Vaccination', cost=50)

        # Make POST request to the view
        response = self.client.post(reverse('order_create'), {
            'pet': pet.id,
            'doctor': self.doctor.id,
            'date': '2024-05-24',
            'services': [service.id]
        })
        order = Order.objects.first()

        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(order.services.count(), 1)

    def test_order_list_view(self):
        # Create an order
        Order.objects.create(doctor=self.doctor, client=self.user.client, date=timezone.now())

        # Make GET request to the view
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['orders']), 1)

    def test_order_detail_view(self):
        # Create an order
        order = Order.objects.create(doctor=self.doctor, client=self.user.client, date=timezone.now())

        # Make GET request to the view
        response = self.client.get(reverse('order_detail', args=[order.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['order'], order)

    def test_order_update_view_GET(self):
        # Create an order
        order = Order.objects.create(doctor=self.doctor, client=self.user.client, date=timezone.now())

        # Make GET request to the view
        response = self.client.get(reverse('order_update', args=[order.id]))
        self.assertEqual(response.status_code, 200)

    # You can continue to add more test cases for POST requests to update orders
    # And more tests for different scenarios and edge cases

