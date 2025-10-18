from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_root_view(request):
    """
    Punto de entrada principal para la API.
    """
    return Response(
        {
            "message": "Bienvenido a la API del Portfolio. Utiliza los siguientes puntos de entrada:",
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
