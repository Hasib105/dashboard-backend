from django import views
from . import views
from django.urls import path, include


urlpatterns = [
    path('', include('djoser.urls')),
    path('jwt/', include('djoser.urls.jwt')),  # JWT endpoints
]
