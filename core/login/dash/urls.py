from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
]
