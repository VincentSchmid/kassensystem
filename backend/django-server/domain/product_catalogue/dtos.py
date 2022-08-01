from uuid import UUID
from ninja import Schema


class SalesTaxReadDto(Schema):
    id: UUID
    name: str
    rate: float


class SalesTaxWriteDto(Schema):
    name: str
    rate: float


class CategoryReadDto(Schema):
    id: UUID
    name: str


class CategoryWriteDto(Schema):
    name: str


class MenuItemReadDto(Schema):
    id: UUID
    name: str
    price: float
    category: CategoryReadDto


class MenuItemWriteDto(Schema):
    name: str
    price: float
    category_id: UUID
