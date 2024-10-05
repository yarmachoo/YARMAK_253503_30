from django.db import models

'''
class Doctor(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='doctors')
    specializations = models.ManyToManyField('DoctorSpecialization', related_name='doctors')
'''

class Department(models.Model):
    name = models.CharField(max_length=100)


class DoctorSpecialization(models.Model):
    name = models.CharField(max_length=100)
