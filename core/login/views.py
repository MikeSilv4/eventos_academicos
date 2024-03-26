from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class EventViewSet(viewsets.ModelViewSet):
    queryset = events.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = EventsSerializerAllFields

class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = organizer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = OrganizerSerializerAllFields

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = participant.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ParticipantsSerializerAllFields

class ParticipantEventViewSet(viewsets.ModelViewSet):
    queryset = participants_events.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ParticipantEventSerializerAllFields
