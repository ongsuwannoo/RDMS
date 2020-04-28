from rest_framework import serializers

from .models import Location

class LocationSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    desc = serializers.CharField()
    logo = serializers.CharField()
