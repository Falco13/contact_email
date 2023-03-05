from django.conf import settings
from time import sleep
from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_email_task(message):
    sleep(3)
    send_mail(
        subject='###--- Email from Contact web-site ---###',
        message=f'\t{message}\n\n ###--- Contact email Web Site! ---###',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
        fail_silently=False,
    )
