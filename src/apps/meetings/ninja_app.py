from ninja import NinjaAPI

from apps.meetings.api.exceptions import set_exceptions
from apps.meetings.api import meeting_router


def get_api():
    api = NinjaAPI()

    set_exceptions(api)

    api.add_router('meetings', meeting_router)

    return api


ninja_api = get_api()
