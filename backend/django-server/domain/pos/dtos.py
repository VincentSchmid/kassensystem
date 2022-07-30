from uuid import UUID
from ninja import Schema


class TableReadDto(Schema):
    id: UUID
    number: int


class TableWriteDto(Schema):
    number: int
