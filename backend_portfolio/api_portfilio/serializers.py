from rest_framework import serializers
from .models import Email


class RootResponseSerializer(serializers.Serializer):
    message = serializers.CharField(help_text="Wellcome to api_portfilio")
    api_entrypoint = serializers.CharField(
        help_text="api_portfilio/api/v1/api_portfilio/"
    )
    admin = serializers.CharField(help_text="/admin/")
    documentation_redoc = serializers.CharField(
        help_text="/api_portfilio/schema/redoc/"
    )
    documentation_swagger = serializers.CharField(
        help_text="/api_portfilio/schema/swagger-ui/"
    )
    documentation_schema_txt = serializers.CharField(help_text="/api_portfilio/schema/")


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"
