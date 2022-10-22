from dataclasses import fields
from rest_framework import serializers
from .models import Contact

# contact serializer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Contact
        fields = '__all__'