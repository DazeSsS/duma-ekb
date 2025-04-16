from datetime import date
from ninja import Schema

from apps.meetings.domain.schemas.base import BaseSchema
from apps.meetings.domain.schemas.question import QuestionResponse


class MeetingResponse(BaseSchema):
    id: int
    date: date
    protocol_number: str
    meeting_type: str
    deputies: int
    presiding: str
    questions: list[QuestionResponse]
