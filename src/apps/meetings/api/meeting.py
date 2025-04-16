from ninja import Router

from apps.meetings.data.models import Meeting
from apps.meetings.domain.schemas import MeetingResponse
from apps.meetings.api.responses import NotFoundResponse


router = Router(
    tags=['Meetings'],
    by_alias=True,
)


@router.get('/', response={200: list[MeetingResponse]})
def list_meetings(request):
    meetings = Meeting.objects.all()
    return meetings


@router.get('/{id}/', response={200: MeetingResponse, 404: NotFoundResponse})
def get_meeting_by_id(request, id: int):
    meeting = Meeting.objects.get(id=id)
    return meeting
