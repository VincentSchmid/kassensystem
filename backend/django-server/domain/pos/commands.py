from uuid import UUID
from django.dispatch import Signal, receiver
from .models import Table, PaymentMethod, Payment, Order, OrderState


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
def handle_delete_payment_method(sender, signal, **kwargs):
    payment_method = PaymentMethod.objects.get(**kwargs)
    payment_method.delete()


@receiver(create_payment_command)
def handle_create_payment(sender, signal, **kwargs):
    payment = Payment.objects.create_payment(**kwargs)
    Order.objects.add_payment(payment)


@receiver(delete_payment_command)
def handle_delete_payment(sender, signal, **kwargs):
    payment = Payment.objects.get(**kwargs)
    payment.delete()


@receiver(create_order_command)
def handle_create_order(sender, signal, **kwargs):
    Order.objects.create(**kwargs)


@receiver(delete_order_command)
def handle_delete_order(sender, signal, **kwargs):
    order = Order.objects.get(**kwargs)
    order.delete()
