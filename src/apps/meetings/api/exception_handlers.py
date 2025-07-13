from ninja import NinjaAPI, Schema
from django.core.exceptions import ObjectDoesNotExist


def set_exceptions(api: NinjaAPI):

    @api.exception_handler(ObjectDoesNotExist)
    def handle_does_not_exist(request, exc):
        return api.create_response(request, NotFoundResponse().model_dump(), status=404)


class NotFoundResponse(Schema):
    message: str = 'Object not found'
