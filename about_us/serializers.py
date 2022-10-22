from rest_framework import serializers
from .models import AboutUs

# About us serializer

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'