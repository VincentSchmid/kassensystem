from django.db.models import QuerySet

from domain.pos.models import Order


def get_order_total(order: Order) -> float:
    return sum([item.menu_item.price * item.quantity for item in order.order_items.all()])

def get_orders_with_order_items() -> QuerySet:
    return Order.objects.prefetch_related("order_items")
