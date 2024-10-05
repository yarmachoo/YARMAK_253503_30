import calendar
import logging
from datetime import datetime

import tzlocal
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from clients.models import Pet
from users.models import Client

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

@login_required
def index(request):
    logging.info("Страница clients/index")
    user_timezone = tzlocal.get_localzone()
    current_date = datetime.now(user_timezone).date()
    current_date_formatted = current_date.strftime("%d/%m/%Y")

    calendar_text = calendar.month(
        datetime.now(user_timezone).year,
        datetime.now(user_timezone).month,
    )

    context = {'calendar': calendar_text}

    search_query = request.GET.get('search', '')  # Получаем поисковый запрос из GET параметра 'search'.
    order = request.GET.get('order', 'name')  # Получаем параметр сортировки из GET параметра 'order'.
    # Фильтруем питомцев по владельцу и поисковому запросу, если таковой есть.
    logging.info("Организация фильтрации и поиска")
    pets = Pet.objects.filter(
        Q(client=request.user.client),
        Q(name__icontains=search_query) | Q(species__icontains=search_query)
    )
    # Сортировка по имени или другому указанному полю.
    pets = pets.order_by(order)
    return render(request, "clients/index.html", {"pets": pets, 'calendar': calendar_text})

@login_required
def create(request):
    logging.info("Страница clients/create")
    create_clients()
    logging.info("Check the POST paramter of create client")
    if request.method == "POST":
        pet = Pet()
        pet.name = request.POST.get("name")
        pet.age = request.POST.get("age")
        pet.species = request.POST.get("species")
        pet.client = request.user.client
        pet.gender = request.POST.get("gender", 'O')  # Установка пола, по умолчанию 'M'
        pet.save()
        return HttpResponseRedirect("/")

    clients = Client.objects.all()
    return render(request, "clients/create.html", {"clients": clients})


def edit(request, id):
    logging.info("Страница clients/edit")
    try:
        pet = Pet.objects.get(id=id)

        if request.method == "POST":
            pet.name = request.POST.get("name")
            pet.age = request.POST.get("age")
            pet.species = request.POST.get("species")
            pet.client = request.user.client
            pet.save()
            logging.info("Все в порядке")
            return HttpResponseRedirect("/")
        else:
            clients = Client.objects.all()
            return render(request, "clients/edit.html", {"pet": pet, "clients": clients})
    except Pet.DoesNotExist:
        logging.exception("Питомец не найден")
        return HttpResponseNotFound("<h2>Pet not found</h2>")


def delete(request, id):
    logging.info("попытка удаления питомца")
    try:
        pet = Pet.objects.get(id=id)
        pet.delete()
        logging.info("попытка удаления питомца прошла успешно")
        return HttpResponseRedirect("/")
    except Pet.DoesNotExist:
        logging.exception("Питомец не найден")
        return HttpResponseNotFound("<h2>Product not found</h2>")

def create_clients():
    if Client.objects.all().count() == 0:
        Client.objects.create(last_name="Yarmak",
                              first_name="Veronika",
                              birth_date="2003-01-01",
                              address="NoInfo")
