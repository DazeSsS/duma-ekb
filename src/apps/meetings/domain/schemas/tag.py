from ninja import Schema


class TagResponse(Schema):
    id: int
    title: str
