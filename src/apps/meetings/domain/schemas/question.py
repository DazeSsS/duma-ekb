from apps.meetings.domain.schemas.base import BaseSchema
from apps.meetings.domain.schemas.tag import TagResponse


class QuestionResponse(BaseSchema):
    id: int
    meeting_id: int
    number: str
    description: str
    quorum: bool
    position_1870: str
    position_1892: str
    author_classification: str
    solution: str
    solution_content: str = ''
    case_number: str
    sheet_numbers: list[float]
    tags: list[TagResponse]
