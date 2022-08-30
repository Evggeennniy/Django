from celery import shared_task
from django.core.mail import send_mail


@shared_task
def sending_mail(subject, email_from, email_to):
    email_subject = "Subject Django Project"
    message = f"""
    Subject : {subject}
    Email from : {email_from}
    Wants to contact
    """

    send_mail(
        email_subject,
        message,
        email_from,
        [email_to],
        fail_silently=False,
    )  # ^ Sending messages
