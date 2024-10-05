import datetime
import re

import phonenumbers
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField

#from doctors.models import Department, DoctorSpecialization
from .models import Client, Doctor


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class':'form-input'}))


    class Meta:
        model =  get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class':'form-input'}))
    this_year = datetime.date.today().year
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year-100, this_year-18))))
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'phone_number', 'date_birth', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password1']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class ClientRegisterForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class':'form-input'}))
    this_year = datetime.date.today().year
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year-100, this_year-18))))

    class Meta:
        model = Client
        model.is_staff = False
        fields = ['username', 'email', 'phone_number', 'date_birth', 'first_name', 'last_name', 'password1', 'password2', 'address']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'address': 'Адрес',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password1']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Таклй E-mail уже существует!")
        return email


class DoctorRegisterForm(UserCreationForm):

    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class':'form-input'}))
    this_year = datetime.date.today().year
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year-100, this_year-18))))
    phone_number = forms.CharField(label="Телефонный номер", widget=forms.TextInput(attrs={'class':'form-input'}))
    is_staff = True
    DEPARTMENT_CHOICES = [
        ('стоматология', 'Стоматология'),
        ('офтальмология', 'Офтальмология'),
        ('общая_практика', 'Общая практика'),
    ]

    department = forms.ChoiceField(
        label="Отделение",
        choices=DEPARTMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-input'})
    )
    class Meta:
        model = Doctor
        model.is_staff = True
        fields = ['photo', 'username', 'email', 'phone_number', 'date_birth', 'first_name', 'last_name',
                  'password1', 'password2', 'department', 'is_staff']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password1']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Таклй E-mail уже существует!")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number:
            if not re.match(r'^\+375(29|33|44|25)\d{7}$', phone_number):
                raise forms.ValidationError("Введите корректный мобильный номер телефона беларусского формата: +375XXXXXXXXX")
        return phone_number
