from typing import Generic, TypeVar
from apps.meetings.domain.schemas.base import BaseSchema


T = TypeVar('T')


class PaginatedResponse(BaseSchema, Generic[T]):
    items: list[T]
    total_pages: int
    current_page: int
