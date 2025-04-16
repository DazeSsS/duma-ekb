from ninja import NinjaAPI
from django.core.exceptions import ObjectDoesNotExist
from apps.meetings.api.responses import NotFoundResponse


def set_exceptions(api: NinjaAPI):
    
    @api.exception_handler(ObjectDoesNotExist)
    def handle_does_not_exist(request, exc):
        return api.create_response(request, NotFoundResponse().model_dump(), status=404)
