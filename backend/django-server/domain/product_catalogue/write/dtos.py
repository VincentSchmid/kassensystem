from uuid import UUID
from ninja import Schema


class SalesTaxReadDto(Schema):
    id: UUID
    name: str
    rate: float


class SalesTaxWriteDto(Schema):
    name: str
    rate: float


class CategoryWriteDto(Schema):
    name: str


class MenuItemWriteDto(Schema):
    name: str
    price: float
    category_id: UUID
