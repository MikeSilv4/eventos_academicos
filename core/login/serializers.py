from rest_framework import serializers
from .models import *

class EventsSerializerAllFields(serializers.ModelSerializer):
    class Meta:
        model = events
        fields = '__all__'

class OrganizerSerializerAllFields(serializers.ModelSerializer):
    class Meta:
        model = organizer
        fields = '__all__'

class ParticipantsSerializerAllFields(serializers.ModelSerializer):
    class Meta:
        model = participant
        fields = '__all__'

class ParticipantEventSerializerAllFields(serializers.ModelSerializer):
    class Meta:
        model = participants_events
        fields = '__all__'