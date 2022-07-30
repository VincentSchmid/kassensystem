from typing import List
from uuid import UUID
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from domain.pos.models import Order
from domain.pos.models import Table


def get_table(id: UUID) -> Table:
    return get_object_or_404(Table, id=id)

def get_tables() -> List[Table]:
    return Table.objects.all()

def get_order_total(order: Order) -> float:
    return sum([item.menu_item.price * item.quantity for item in order.order_items.all()])

def get_orders_with_order_items() -> QuerySet:
    return Order.objects.prefetch_related("order_items")
