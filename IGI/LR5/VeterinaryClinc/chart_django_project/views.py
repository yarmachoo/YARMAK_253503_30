from django.shortcuts import render

from news.models import Articles

from appointments.models import Service


"""def index(request):
    data = "Current Data"
    services = Service.objects.all()
    context = {
        "services": services
    }
    return render(request, 'chart_django_project/index.html', context)"""

import matplotlib.pyplot as plt
import io
import urllib, base64

def index(request):
    # Подготовьте данные для графика, например, из модели Django
    services = Service.objects.all()
    labels = [service.name for service in services]
    data = [service.cost for service in services]

    # Создайте график с использованием Matplotlib
    fig, ax = plt.subplots()
    ax.bar(labels, data)
    ax.set_ylabel('Costs')
    ax.set_title('Costs by service')
    ax.set_xticks(labels)
    ax.set_xticklabels(labels, rotation='vertical')

    # Сохраните график в виртуальный файл в формате PNG
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Кодирование изображения в base64 и подготовка его к вставке в HTML
    string = base64.b64encode(buffer.read())
    img_url = urllib.parse.quote(string)

    # Возвращаем данные графика в контекст
    context = {'img_url': img_url}
    return render(request, 'chart_django_project/index.html', context)


