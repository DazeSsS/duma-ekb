from ninja import Schema


class NotFoundResponse(Schema):
    message: str = 'Object not found'
