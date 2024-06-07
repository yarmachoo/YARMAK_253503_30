from django.contrib import admin

from appointments.models import Service

from appointments.models import ServiceCategory

from appointments.models import Order

from appointments.models import OrderService

admin.site.register(Service)

admin.site.register(ServiceCategory)

admin.site.register(Order)

admin.site.register(OrderService)
