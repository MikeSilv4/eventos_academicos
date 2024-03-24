from django.urls import path, include
from rest_framework.routers  import DefaultRouter
from .views import *

routers = DefaultRouter()
routers.register(r'events', EventViewSet, basename='eventURL')

urlpatterns = [
    path('', include(routers.urls)),
]
