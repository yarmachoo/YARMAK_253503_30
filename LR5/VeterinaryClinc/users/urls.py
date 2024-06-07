from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('preregistration/', views.preregistration, name='preregistration'),
    path('registerclient/', views.RegisterClient.as_view(), name='registerclient'),
    path('registerdoctor/', views.RegisterDoctor.as_view(), name='registerdoctor'),
    path('list_doctors/', views.list_doctors, name='list_doctors')
]

