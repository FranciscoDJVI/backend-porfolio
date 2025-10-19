from celery import shared_task, app
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Email
from smtplib import SMTPException


@shared_task(bind=True)
def send_notification_email(self, email_id):
    # Send notification when any user send a email.
    """
    Tarea Celery para enviar el correo. Recibe el ID del registro
    para cargar la instancia y evitar problemas de serialización.
    """
    try:
        email_data = Email.objects.get(pk=email_id)
        if email_data:
            body_message = email_data.message
            recipient_email = email_data.email_contact

            email = EmailMessage(
                subject=email_data.subject,
                body=body_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[recipient_email],
            )
            email.send(fail_silently=False)
            print(f"Correo de confirmación enviado exitosamente a {recipient_email}")
            return "Email sent successfully"
        else:
            return f"Error: No se encontró el email con ID {email_id}"
    except Exception as e:
        self.retry(exc=e, countdown=60)  # Resend in 60 seconds
