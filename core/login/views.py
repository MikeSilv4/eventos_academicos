from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class EventViewSet(viewsets.ModelViewSet):
    queryset = events
    permission_classes = (IsAuthenticated,)
    serializer_class = EventsSerializerAllFields
