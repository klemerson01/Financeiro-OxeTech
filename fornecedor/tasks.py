from celery import shared_task
from django.core.mail import send_mail
import time
from django.conf import settings

@shared_task
def add():
    print('Started task, processing...')
    time.sleep(15)
    print('Finished Task')
    return True


@shared_task
def enviar_email(assunto, mensagem, destinatario):
    send_mail(
        subject=assunto,
        message=mensagem,
        from_email='nfe@computek.tech',
        recipient_list=[destinatario],
        fail_silently=False,
    )