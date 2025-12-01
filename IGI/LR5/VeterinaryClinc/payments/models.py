from django.db import models
from django.conf import settings

class Payment(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255)
    tx_signature = models.CharField(max_length=255)
    amount = models.IntegerField()      # amount в токенах (например 150)
    service_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_id} — {self.client}"
