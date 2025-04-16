from django.urls import path
from apps.meetings.ninja_app import ninja_api

urlpatterns = [
    path('', ninja_api.urls),
]
