from django.urls import path
from . import views

urlpatterns = [
    path('article', views.index, name='article-index'),
]