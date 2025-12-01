from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Payment
from django.contrib.auth import get_user_model

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import subprocess
import json
from .models import Payment
from django.contrib.auth import get_user_model

User = get_user_model()

@csrf_exempt
def confirm_payment(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=400)

    data = json.loads(request.body)

    user = User.objects.get(id=data["client_id"])

    Payment.objects.create(
        client=user,
        payment_id=data["payment_id"],
        tx_signature=data["tx_signature"],
        amount=data["amount"],
        service_name=data["service_name"],
    )

    return JsonResponse({"status": "ok"})


@login_required
def pay_page(request):
    return render(request, "payments/pay.html")

@csrf_exempt
def start_payment(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=400)

    data = json.loads(request.body)
    user = User.objects.get(id=data["client_id"])

    try:
        result = subprocess.run(
            [
                "npx", "ts-node",
                "/home/vero/cmpt130/7sem/TOFD/L2/new-dex-app/client/payment.ts",
                str(data["amount"]),
                data["client_pubkey"],
                data["service_name"],
            ],
            capture_output=True,
            text=True,
            check=True,
            cwd="/home/vero/cmpt130/7sem/TOFD/L2/new-dex-app"
        )

        output = json.loads(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        return JsonResponse({"error": e.stderr}, status=500)

    Payment.objects.create(
        client=user,
        payment_id=str(data["client_id"]) + "_" + str(data["amount"]),
        tx_signature="",
        amount=data["amount"],
        service_name=data["service_name"],
    )

    return JsonResponse(output)


def consultations_view(request):
    # считаем количество оплаченных, но не использованных консультаций
    consultations_count = Payment.objects.filter(
        service_name="Consultation",
        #status="Paid",
        client=request.user
    ).count()

    return render(request, "payments/consultations.html", {
        "consultations_count": consultations_count
    })

def use_consultation(request):
    # ищем первую доступную консультацию
    consultation = Payment.objects.filter(
        service_name="Consultation",
        client=request.user
    ).first()

    if consultation:
        # здесь можно добавить поле status в модель, чтобы отмечать "Used"
        # пока просто удалим запись или оставим сообщение
        consultation.delete()
        message = "Вы успешно использовали консультацию!"
    else:
        message = "У вас нет доступных консультаций."

    return render(request, "payments/use.html", {"message": message})
