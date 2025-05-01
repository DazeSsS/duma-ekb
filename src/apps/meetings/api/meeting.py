from django.core.paginator import Paginator
from ninja import Router

from apps.meetings.data.models import Meeting
from apps.meetings.domain.schemas import MeetingResponse, PaginatedResponse
from apps.meetings.api.responses import NotFoundResponse


router = Router(
    tags=['Meetings'],
    by_alias=True,
)


@router.get('/', response={200: PaginatedResponse[MeetingResponse]})
def list_meetings(request, page: int = 1, per_page: int = 10):
    meetings = Meeting.objects.all()
    paginator = Paginator(meetings, per_page)
    page_obj = paginator.get_page(page)
    
    return PaginatedResponse[MeetingResponse](
        items=list(page_obj.object_list),
        total_pages=paginator.num_pages,
        current_page=page_obj.number
    )


@router.get('/{id}/', response={200: MeetingResponse, 404: NotFoundResponse})
def get_meeting_by_id(request, id: int):
    meeting = Meeting.objects.get(id=id)
    return meeting
