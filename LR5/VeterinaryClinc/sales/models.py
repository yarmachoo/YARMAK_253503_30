from django.db import models

from appointments.models import Service

from users.models import Client


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sales')
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    services = models.ManyToManyField(Service, through='SaleService')


class SaleService(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sale_services')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
