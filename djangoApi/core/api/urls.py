from django.urls import path, include
from rest_framework.routers import DefaultRouter
from concerts.api.urls import concert_router

router = DefaultRouter()
router.registry.extend(concert_router.registry)

urlpatterns = [
    path('', include(router.urls))
]