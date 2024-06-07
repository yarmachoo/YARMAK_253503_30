from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Client, Doctor

admin.site.register(User, UserAdmin)
admin.site.register(Client)
admin.site.register(Doctor)
