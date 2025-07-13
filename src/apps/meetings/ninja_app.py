from ninja import NinjaAPI

from apps.meetings.api.exception_handlers import set_exceptions
from apps.meetings.api.routers import meeting_router


def get_api():
    api = NinjaAPI()

    set_exceptions(api)

    api.add_router('meetings', meeting_router)

    return api


ninja_api = get_api()
