import logging

from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from clients.models import Pet

from doctors.models import Department

from users.models import Client, Doctor
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


def index(request):
    logging.info("Show departments")
    departments = Department.objects.all()
    return render(request, "doctors/index.html", {"departments": departments})


def create(request):
    create_doctors()
    logging.info("Check the POST parameter of create pet")
    if request.method == "POST":
        logging.info("Add new pet")
        department = Department()
        department.name = request.POST.get("name")
        pet.age = request.POST.get("age")
        pet.species = request.POST.get("species")
        pet.client_id = request.POST.get("client")
        pet.save()
        return HttpResponseRedirect("/")

    clients = Client.objects.all()
    return render(request, "clients/create.html", {"clients": clients})


def edit(request, id):
    try:
        logging.info("try to edit pet")
        pet = Pet.objects.get(id=id)
        logging.info("Check the POST parameter of edit pet")
        if request.method == "POST":
            pet.name = request.POST.get("name")
            pet.age = request.POST.get("age")
            pet.species = request.POST.get("species")
            pet.client_id = request.POST.get("client")
            pet.save()
            return HttpResponseRedirect("/")
        else:
            logging.info("parameter of edit pet is not POST")
            clients = Client.objects.all()
            return render(request, "clients/edit.html", {"pet": pet, "clients": clients})
    except Pet.DoesNotExist:
        logging.exception("Pet does not exist")
        return HttpResponseNotFound("<h2>Product not found</h2>")


def delete(request, id):
    try:
        logging.info("Try to delete pet")
        pet = Pet.objects.get(id=id)
        pet.delete()
        return HttpResponseRedirect("/")
    except Pet.DoesNotExist:
        logging.exception("Exception of delete pet")
        return HttpResponseNotFound("<h2>Product not found</h2>")

def create_doctors():
    if Doctor.objects.all().count() == 0:
        Doctor.objects.create(last_name="Yarmak",
                              first_name="Veronika",
                              birth_date="2003-01-01",
                              address="NoInfo")

