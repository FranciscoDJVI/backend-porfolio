from rest_framework import viewsets
from .serializers import EmailSerializer
from .models import Email
from ..tasks import send_notification_email


class EmailViewSet(viewsets.ModelViewSet):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()

        send_notification_email.delay(instance.id)
