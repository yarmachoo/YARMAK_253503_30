import datetime

from django.db import models
from users.models import Client
from tzlocal import get_localzone
import pytz

class Pet(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    age = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now(), verbose_name="Дата добавления питомца")

    def get_local_time(self):
        local_tz = get_localzone()  # тут я получаю место (Europe/minks)
        local_time = self.create_date.astimezone(local_tz)
        return local_time.strftime('%d-%m-%Y %H:%M:%S')

    def get_utc_time(self):
        local_time = self.create_date.astimezone(pytz.utc)
        return local_time.strftime('%d-%m-%Y %H:%M:%S')
