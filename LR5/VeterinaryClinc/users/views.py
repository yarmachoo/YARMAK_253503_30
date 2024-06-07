import logging

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import LoginUserForm, RegisterUserForm, ClientRegisterForm, DoctorRegisterForm
from .models import Doctor
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

def preregistration(request):
    logging.info("Preregistration form")
    return render(request, "users/preregistration.html", )
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        logging.info("registration is success")
        return reverse_lazy('home')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}

    success_url = reverse_lazy('users:login')

class RegisterClient(CreateView):
    form_class = ClientRegisterForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация клиента"}

    success_url = reverse_lazy('users:login')

class RegisterDoctor(CreateView):
    form_class = DoctorRegisterForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация доктора"}

    success_url = reverse_lazy('users:login')


def list_doctors(request):
    logging.info("Show doctors list")
    doctors = Doctor.objects.all()
    return render(request, 'users/list_doctor.html', {'doctors': doctors})
