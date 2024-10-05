from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='clients_home'),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit, name='edit'),
    path("delete/<int:id>/", views.delete),
]