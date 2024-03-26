from django.urls import path, include
from rest_framework.routers  import DefaultRouter
from .views import *

routers = DefaultRouter()
routers.register(r'event', EventViewSet, basename='event')
routers.register(r'organizer', OrganizerViewSet, basename='organizer')
routers.register(r'participant', ParticipantViewSet, basename='participant')
routers.register(r'participant_event', ParticipantEventViewSet, basename='participant_event')

urlpatterns = [
    path('', include(routers.urls)),
]
