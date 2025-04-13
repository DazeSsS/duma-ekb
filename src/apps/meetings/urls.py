from django.urls import path
from ninja import NinjaAPI

from apps.meetings.api import meeting_router

api = NinjaAPI()
api.add_router('/meetings', meeting_router)

urlpatterns = [
    path('', api.urls),
]
