from rest_framework.decorators import api_view
from .serializers import ConcertSerializer, BandSerializer, VenueSerializer
from ..models import Concert, Band, Venue

from rest_framework.viewsets import ModelViewSet

class ConcertViewSet(ModelViewSet):
  queryset = Concert.objects.all()
  serializer_class = ConcertSerializer
