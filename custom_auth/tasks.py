from django.core.mail import send_mail
from Epam_hacknu.celery import app


@app.task()
def send_email_task(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)