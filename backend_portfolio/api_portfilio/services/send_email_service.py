from django.core.mail import send_mail
from django.conf import settings
from api_portfilio.models import Email


def send_notification_email(email_id):
    try:
        email_data = Email.objects.get(pk=email_id)
        if email_data:
            body_message = email_data.message
            recipient_email = email_data.email_contact
            send_mail(
                email_data.subject,
                body_message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient_email],
                fail_silently=False,
            )
            return "Email sent successfully"
        else:
            return f"Error: No se encontró el email con ID {email_id}"
    except Exception as e:
        print(f"Error sending email: {e}")
