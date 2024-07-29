from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InteriorDesignerViewSet

router = DefaultRouter()
router.register(r"designers", InteriorDesignerViewSet, basename="interiordesigner")

urlpatterns = [
    path("", include(router.urls)),
]
