from ninja import Router

from apps.meetings.data.models import Meeting
from apps.meetings.domain.schemas import MeetingResponse


router = Router(
    tags=['Meetings'],
)

@router.get('/', response={200: list[MeetingResponse]})
def list_meetings(request):
    meetings = Meeting.objects.all()
    return meetings
