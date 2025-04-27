from typing import Literal
from datetime import date
from ninja import Schema

from apps.meetings.domain.schemas.base import BaseSchema
from apps.meetings.domain.schemas.question import QuestionResponse
from apps.meetings.domain.enums import MeetingType


class MeetingResponse(BaseSchema):
    id: int
    date: date
    meeting_type: Literal[*MeetingType.values]
    deputies: int
    presiding: str
    questions: list[QuestionResponse]
