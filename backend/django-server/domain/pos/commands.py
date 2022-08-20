from uuid import UUID
from typing import List

from django.dispatch import Signal, receiver
from .models import Table, PaymentMethod, Payment, Order, OrderItem
from domain.product_catalogue.read.models import MenuItem
from domain.employee.models import Waiter
from .dtos import OrderItemWriteDto


create_table_command = Signal()
delete_table_command = Signal()

create_payment_method_command = Signal()
delete_payment_method_command = Signal()

create_payment_command = Signal()
delete_payment_command = Signal()

create_order_command = Signal()
delete_order_command = Signal()


@receiver(create_table_command)
def handle_create_table(sender, signal, **kwargs):
    Table.objects.create(**kwargs)


@receiver(delete_table_command)
def handle_delete_table(sender, signal, **kwargs):
    table = Table.objects.get(**kwargs)
    table.delete()


@receiver(create_payment_method_command)
def handle_create_payment_method(sender, signal, **kwargs):
    PaymentMethod.objects.create(**kwargs)


@receiver(delete_payment_method_command)
def handle_delete_payment_method(sender, signal, payment_method_id: UUID, **kwargs):
    payment_method = PaymentMethod.objects.get(id=payment_method_id)
    payment_method.delete()


@receiver(create_payment_command)
def handle_create_payment(
    sender,
    signal,
    payment_id: UUID,
    payment_method_id: UUID,
    order_id: UUID,
    amount: int,
    **kwargs
):
    payment_method = PaymentMethod.objects.get(id=payment_method_id)
    payment = Payment.objects.create_payment(
        id=payment_id, payment_method=payment_method, order_id=order_id, amount=amount
    )
    Order.objects.add_payment(payment)


@receiver(delete_payment_command)
def handle_delete_payment(sender, signal, payment_id, **kwargs):
    payment = Payment.objects.get(id=payment_id)
    payment.delete()


@receiver(create_order_command)
def handle_create_order(
    sender,
    signal,
    order_id: UUID,
    user_id: UUID,
    table_id: UUID,
    order_items: List[OrderItemWriteDto],
    **kwargs
):
    waiter = Waiter.objects.get(user_id=user_id)
    table = Table.objects.get(id=table_id)
    order = Order.objects.create(waiter=waiter, table=table, id=order_id)
    for order_item in order_items:
        create_order_item(order, order_item)


def create_order_item(order: Order, order_item: OrderItemWriteDto):
    menu_item = MenuItem.objects.get(id=order_item.menu_item_id)
    OrderItem.objects.create(
        order=order, menu_item=menu_item, quantity=order_item.quantity
    )


@receiver(delete_order_command)
def handle_delete_order(sender, signal, order_id: UUID, **kwargs):
    order = Order.objects.get(id=order_id)
    order.delete()
