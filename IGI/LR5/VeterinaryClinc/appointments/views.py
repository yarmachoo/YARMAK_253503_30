import datetime
import logging

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from .models import Service, ServiceCategory, Order, OrderService
from .forms import ServiceForm
from clients.models import Pet

from users.models import Doctor
from users.models import Client
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
@login_required
def doctors_schedule(request):
    logging.info("Обращение к doctors_schedule")
    doctor = request.user.doctor
    orders_before_today = Order.objects.filter(doctor=doctor, date__lt=datetime.date.today())
    orders_today = Order.objects.filter(doctor=doctor, date=datetime.date.today())
    orders_tomorrow = Order.objects.filter(doctor=doctor, date=datetime.date.today() + datetime.timedelta(days=1))
    orders_after_tomorrow = Order.objects.filter(doctor=doctor,
                                                 date__gt=datetime.date.today() + datetime.timedelta(days=1))

    context = {
        'doctor': doctor,
        'orders_before_today': orders_before_today,
        'orders_today': orders_today,
        'orders_tomorrow': orders_tomorrow,
        'orders_after_tomorrow': orders_after_tomorrow,
    }
    logging.info("Возврат страницы")
    return render(request, 'doctors_schedule.html', context)
@login_required
def order_create(request):
    logging.info("Обращение к order_create")
    if request.method == 'POST':
        client = request.user.client
        pet_id = request.POST.get('pet')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        service_ids = request.POST.getlist('services')

        pet = client.pet_set.get(id=pet_id)
        doctor = Doctor.objects.get(id=doctor_id)
        services = Service.objects.filter(id__in=service_ids)  # Извлечь все услуги одним запросом
        total_cost = services.aggregate(Sum('cost'))['cost__sum'] or 0  # Рассчитать общую стоимость
        order = Order.objects.create(client=client, pet=pet, doctor=doctor, date=date, total_cost=total_cost)

        # Создать связи OrderService для всех выбранных услуг
        OrderService.objects.bulk_create(
            [OrderService(order=order, service=service) for service in services]
        )
        logging.info("Обращение прошло успешно")
        return redirect('order_list')
    else:
        client = request.user.client
        pets = client.pet_set.all()
        doctors = Doctor.objects.all()
        services = Service.objects.all()
        logging.info("метод не POST")
        return render(request, 'order_create.html', {'pets': pets, 'doctors': doctors, 'services': services})


@login_required
def order_list(request):
    logging.info("Обращение к order_list")
    orders = Order.objects.filter(client=request.user.client)
    return render(request, 'order_list.html', {'orders': orders})


@login_required
def order_detail(request, pk):
    logging.info("Обращение к order_detail")
    order = get_object_or_404(Order, pk=pk)
    order = Order.objects.get(id=pk)
    return render(request, 'order_detail.html', {'order': order})


@login_required
def order_update(request, pk):
    logging.info("Обращение к order_update")
    order = get_object_or_404(Order, pk=pk)
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        pet_id = request.POST.get('pet')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        service_ids = request.POST.getlist('services')

        pet = Pet.objects.get(id=pet_id)
        doctor = Doctor.objects.get(id=doctor_id)
        order.pet = pet
        order.doctor = doctor
        order.date = date
        order.save()

        order.services.clear()
        for service_id in service_ids:
            service = Service.objects.get(id=service_id)
            OrderService.objects.create(order=order, service=service)

        return redirect('order_list')
    else:
        client = request.user.client
        pets = client.pet_set.all()
        doctors = Doctor.objects.all()
        services = Service.objects.all()
        return render(request, 'order_update.html', {'order': order, 'pets': pets, 'doctors': doctors, 'services': services})


@login_required
def order_delete(request, pk):
    logging.info("Обращение к order_delete")
    order = get_object_or_404(Order, pk=pk)
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('order_list')


@login_required
def service_detail(request, pk):
    logging.info("Обращение к service_detail")
    service = Service.objects.get(id=pk)
    return render(request, 'service_detail.html', {'service': service})

@login_required
def service_create(request):
    logging.info("Обращение к service_create")
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'service_create.html', {'form': form})

@login_required
def service_list(request):
    logging.info("Обращение к service_list")
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})


@login_required
def service_update(request, pk):
    logging.info("Обращение к service_update")
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service_update.html', {'form': form})


@login_required
def service_delete(request, pk):
    logging.info("Обращение к service_delete")
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'service_delete.html', {'service': service})

@login_required
def order_pay(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Здесь добавьте логику для перехода на страницу оплаты
    if request.method == 'POST':
        # Логика успешной оплаты
        order.is_payed = True
        order.save()
        return redirect('order_list')  # Перенаправьте на страницу с заказами

    return render(request, 'pay.html', {'order': order})