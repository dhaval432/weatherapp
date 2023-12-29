from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
# API_KEY = settings.WEATHER_API_KEY