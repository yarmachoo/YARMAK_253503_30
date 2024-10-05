from django.contrib import admin

from doctors.models import Department, DoctorSpecialization

admin.site.register(Department)

admin.site.register(DoctorSpecialization)