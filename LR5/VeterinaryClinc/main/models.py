from django.db import models

from VeterinaryClinc import settings


class Questions(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class PromoCode(models.Model):
    promocode = models.CharField(max_length=50)
    percent = models.IntegerField()



class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    date = models.DateField()

