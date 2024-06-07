from PIL.Image import Image
from django.contrib.auth.models import AbstractUser
from django.db import models
#from doctors.models import Department, DoctorSpecialization


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")
    is_staff = models.BooleanField(default=False)


class Client(User):
    address = models.CharField(max_length=255)
    promocode = models.CharField(max_length=255, null=True)
    def __str__(self):
        return f'{self.last_name}'


class Doctor(User):
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", default=None,
                              blank=True, null=True, verbose_name="Фотография")
    department = models.CharField(max_length=255)
    specializations = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.last_name}'

