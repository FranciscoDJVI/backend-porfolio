from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from api_portfilio import views

router = routers.DefaultRouter()
router.register(r"api_portfilio", views.EmailViewSet, "api_portfilio")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Documentation portfolio API")),
]
