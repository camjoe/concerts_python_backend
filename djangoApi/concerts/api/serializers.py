from rest_framework import serializers
from ..models import Band, Concert, Venue

class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = '__all__'

class BandSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Band
      fields = '__all__'

class ConcertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Concert 
        fields = '__all__'
        depth = 1