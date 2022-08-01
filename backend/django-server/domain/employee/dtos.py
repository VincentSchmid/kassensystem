from uuid import UUID
from ninja import Schema


class WaiterReadDto(Schema):
    id: UUID
    name: str
    user_id: UUID


class WaiterWriteDto(Schema):
    name: str
    user_id: UUID


class ManagerReadDto(Schema):
    id: UUID
    name: str
    user_id: UUID


class ManagerWriteDto(Schema):
    name: str
    user_id: UUID
