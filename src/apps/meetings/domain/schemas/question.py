from typing import Literal
from pydantic import field_serializer

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
    sheet_numbers: str
    tags: list[TagResponse]

    @field_serializer('sheet_numbers')
    def convert_sheet_numbers(self, sheet_numbers: list[str]):
        if sheet_numbers[0] == sheet_numbers[1]:
            return sheet_numbers[0].replace('.5', ' об')
        return ' - '.join(number.replace('.5', ' об') for number in sheet_numbers)
