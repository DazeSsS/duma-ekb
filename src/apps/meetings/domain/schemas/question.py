from ninja import Schema

from apps.meetings.domain.schemas.tag import TagResponse


class QuestionResponse(Schema):
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
