from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def add(x, y):
    print(f"args {x} and {y}")
    sleep(5)
    # raise ValueError("Ошибка")
    return x + y


@shared_task
def send_otp_mail(email, code):
    print(10* "%")
    send_mail(
        "Registration for you",
        f"ващ одноразовый код: {code}.",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return "OK"

@shared_task
def send_daily_report():
    send_mail(
        "Report excel",
        "то что должно всегда происходить _",
        settings.EMAIL_HOST_USER,
        ["karataevbekbolsun@gmail.com"],
        fail_silently=False,
    )
    return "OK"
