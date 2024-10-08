from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('cat_fact', views.cat_fact_view, name='cat_fact'),
    path('random_dog', views.random_dog_view, name='random_dog'),
    path('questions/', views.questions_list, name='questions_list'),
    path('vacancies/', views.VacancyListView.as_view(), name='vacancy-list'),
    path('vacancies/<int:pk>/', views.VacancyDetailView.as_view(), name='vacancy-detail'),
    path('promocodes/', views.promocode_list, name='promocode-list'),
    path('reviews/', views.reviews_list, name='reviews-list'),
    path('policy/', views.policy, name='policy'),
]