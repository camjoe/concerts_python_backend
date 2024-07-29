from rest_framework.routers import DefaultRouter
from .views import ConcertViewSet

concert_router = DefaultRouter()
concert_router.register(r'concerts', ConcertViewSet)
#concert_router.register(r'bands', ConcertViewSet)
#concert_router.register(r'venues', ConcertViewSet)