from asyncio.windows_events import NULL

from django.db import models
from django.db.models import Sum
from django.urls import reverse

from clients.models import Pet
from users.models import Client, Doctor

from main.models import PromoCode


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Service(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')


    def __str__(self):
        return f'{self.name} costs {self.cost}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    services = models.ManyToManyField(Service, through='OrderService')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    is_payed = models.BooleanField(default=False)  # Новое поле
    def __str__(self):
        return f'{self.date}'

    def save(self, *args, **kwargs):
        discount = 1.0
        if self.pk:
            if self.client.promocode:
                try:
                    promo = PromoCode.objects.get(promocode=self.client.promocode)
                    discount = (self.total_cost * promo.percent) / 100
                except PromoCode.DoesNotExist:
                    pass

            self.total_cost = self.services.aggregate(total=Sum('cost'))['total'] or 0.00
            if self.client.promocode is not NULL:
                discount = (self.total_cost * promo.percent) / 100
                self.total_cost -= discount

        super().save(*args, **kwargs)

class OrderService(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
