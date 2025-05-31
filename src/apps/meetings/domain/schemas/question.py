from typing import Literal

from apps.meetings.domain.schemas.base import BaseSchema
from apps.meetings.domain.schemas.tag import TagResponse
from apps.meetings.domain.enums import (
    AuthorClassification,
    Position1870,
    Position1892,
    Solution,
)


class QuestionResponse(BaseSchema):
    id: int
    meeting_id: int
    number: str
    description: str
    quorum: bool
    position_1870: Literal[*Position1870.values, '']
    position_1892: Literal[*Position1892.values, '']
    author_classification: Literal[*AuthorClassification.values, '']
    solution: Literal[*Solution.values, '']
    solution_content: str = ''
    sheet_numbers: list[float]
    tags: list[TagResponse]
