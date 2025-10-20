from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from api_portfilio.serializers import RootResponseSerializer


@extend_schema(
    responses={200: RootResponseSerializer},
)
@api_view(["GET"])
def api_root_view(request):
    """
    entryendponits for the API.
    """
    return Response(
        {
            "message": "Wellcome to the API of my personal portfolio. use the next entryendponits:",
            "api_entrypoint": "api_portfilio/api/v1/api_portfilio/",
            "admin": "/admin/",
            "documentation redoc": "/api_portfilio/schema/redoc/",
            "documentation swagger": "/api_portfilio/schema/swagger-ui/",
            "documentation schema.txt": "/api_portfilio/schema/",
        }
    )


urlpatterns = [
    path("", api_root_view),
    path("admin/", admin.site.urls),
    path("api_portfilio/", include("api_portfilio.urls")),
]
