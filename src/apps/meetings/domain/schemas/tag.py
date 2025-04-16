from apps.meetings.domain.schemas.base import BaseSchema


class TagResponse(BaseSchema):
    id: int
    title: str
