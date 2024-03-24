from rest_framework import serializers
from .models import *

class EventsSerializerAllFields(serializers.ModelSerializer):
    class Meta:
        model = events
        fields = '__all__'