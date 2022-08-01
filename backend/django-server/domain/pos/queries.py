from typing import List
from uuid import UUID
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from domain.pos.models import Order, Table, PaymentMethod, Payment


def get_table(id: UUID) -> Table:
    return get_object_or_404(Table, id=id)


def get_tables() -> List[Table]:
    return Table.objects.all()


def get_payment_method(id: UUID) -> PaymentMethod:
    return PaymentMethod.objects.get(id=id)


def get_payment_methods() -> List[PaymentMethod]:
    return PaymentMethod.objects.all()


def get_payment(order_id: UUID) -> PaymentMethod:
    return Payment.objects.get_payment(order_id=order_id)


def get_order(id: UUID) -> Order:
    return get_orders_with_order_items().get(id=id)


def get_orders() -> List[Order]:
    return get_orders_with_order_items().all()


def get_order_total(order: Order) -> float:
    return sum(
        [item.menu_item.price * item.quantity for item in order.order_items.all()]
    )


def get_orders_with_order_items() -> QuerySet:
    return Order.objects.prefetch_related("order_items")
