from typing import List
from uuid import UUID
from ninja import Schema

from domain.employee.dtos import WaiterReadDto


class TableReadDto(Schema):
    id: UUID
    number: int


class TableWriteDto(Schema):
    number: int


class PaymentMethodReadDto(Schema):
    id: UUID
    name: str


class PaymentMethodWriteDto(Schema):
    name: str


class OrderItemReadDto(Schema):
    id: UUID
    menu_item_id: UUID
    quantity: int


class OrderItemWriteDto(Schema):
    menu_item_id: UUID
    quantity: int


class PaymentReadDto(Schema):
    id: UUID
    amount: float
    payment_method: PaymentMethodReadDto


class PaymentWriteDto(Schema):
    amount: float
    payment_method_id: UUID


class OrderReadDto(Schema):
    id: UUID
    order_items: List[OrderItemReadDto]
    table: TableReadDto
    status: str
    waiter: WaiterReadDto
    payment: PaymentReadDto


class OrderWriteDto(Schema):
    order_items: List[OrderItemWriteDto]
    table_id: UUID
    status: str
    waiter_id: UUID
