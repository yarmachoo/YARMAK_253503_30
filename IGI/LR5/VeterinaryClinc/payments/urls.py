from django.urls import path
from .views import (confirm_payment,
                    pay_page,
                    start_payment,
                    consultations_view,
                    use_consultation)

urlpatterns = [
    path("start/", start_payment, name="start_payment"),
    path("confirm/", confirm_payment, name="confirm_payment"),
    path("pay/", pay_page, name="pay_page"),
    path("consultations/", consultations_view, name="consultations"),
    path("use/", use_consultation, name="use_consultation"),
]
