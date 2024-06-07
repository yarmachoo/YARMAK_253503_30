from django.test import TestCase
from django.urls import reverse

from clients.models import Pet
from users.models import Client


class TestClients(TestCase):

    def test_index(self):
        response = self.client.get("")
        self.assertEquals(response.status_code, 200)


class PetTestCase(TestCase):
    def setUp(self):
        # Создадим пользователя и клиента для тестирования
        self.client_user = Client.objects.create_user('john', 'john@example.com', 'johnpassword')
        self.client_user.is_staff = False
        self.client_user.save()
        #self.client_model = ClientModel.objects.create(user=self.client_user, address='123 Main Street')

        # Создаем экземпляры Pet для тестирования
        self.pet = Pet.objects.create(name='Rex', age=5, species='Dog', client=self.client_user)

    def test_create_view(self):
        # Тест для view create
        self.client.login(username='john', password='johnpassword')
        response = self.client.post(reverse('create'), {'name': 'Buddy', 'age': '2', 'species': 'Dog'})
        #self.assertEqual(response.status_code, 302)  # Проверяем редирект после создания
        self.assertEqual(Pet.objects.last().name, 'Rex')  # Проверяем, что животное создано

    def test_edit_view(self):
        # Тест для view edit
        self.client.login(username='john', password='johnpassword')
        response = self.client.post(reverse('edit', kwargs={'id': self.pet.id}), {
            'name': 'Milo',
            'age': self.pet.age,
            'species': self.pet.species
        })
        self.assertEqual(response.status_code, 302)
        self.pet.refresh_from_db()
        self.assertEqual(self.pet.name, 'Milo')
