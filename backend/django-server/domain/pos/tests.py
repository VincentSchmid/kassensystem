from uuid import uuid4
from django.test import TestCase

from domain.product_catalogue.models import MenuItem
from domain.employee.models import Waiter
from .models import Order, OrderItem, Table, PaymentMethod, Payment
from .dtos import OrderItemWriteDto
from .commands import (
    create_table_command,
    delete_table_command,
    create_payment_method_command,
    delete_payment_method_command,
    create_payment_command,
    delete_payment_command,
    create_order_command,
    delete_order_command,
)
from .queries import (
    get_order_total,
    get_orders_with_order_items,
    get_orders,
    get_order,
    get_table,
    get_tables,
    get_payment_method,
    get_payment_methods,
    get_payment,
    get_order_add_total,
)


class CommandTestCases(TestCase):
    def test_create_table_command(self):
        table_id = uuid4()
        create_table_command.send(sender=None, id=table_id, number=12)
        self.assertIsNotNone(Table.objects.get(id=table_id))

    def test_delete_table_command(self):
        table_id = uuid4()
        Table.objects.create(id=table_id, number=12)
        delete_table_command.send(sender=None, id=table_id)
        self.assertIsNone(Table.objects.filter(id=table_id).first())

    def test_create_payment_method_command(self):
        payment_method_id = uuid4()
        create_payment_method_command.send(
            sender=None, id=payment_method_id, name="Cash"
        )
        self.assertIsNotNone(PaymentMethod.objects.get(id=payment_method_id))

    def test_delete_payment_method_command(self):
        payment_method_id = uuid4()
        PaymentMethod.objects.create(id=payment_method_id, name="Cash")
        delete_payment_method_command.send(
            sender=None, payment_method_id=payment_method_id
        )
        self.assertIsNone(PaymentMethod.objects.filter(id=payment_method_id).first())

    def test_create_payment_command(self):
        order_id = uuid4()
        payment_id = uuid4()
        payment_method_id = uuid4()
        order_id = uuid4()
        payment_method = PaymentMethod.objects.create(id=payment_method_id, name="Cash")
        table = Table.objects.create(id=order_id, number=12)
        waiter = Waiter.objects.create(id=order_id, name="John")
        order = Order.objects.create(id=order_id, waiter=waiter, table=table)

        create_payment_command.send(
            sender=None,
            payment_id=payment_id,
            payment_method_id=payment_method_id,
            order_id=order_id,
            amount=100,
        )

        self.assertIsNotNone(Payment.objects.get(id=payment_id))

    def test_delete_payment_command(self):
        order_id = uuid4()
        payment_id = uuid4()
        payment_method_id = uuid4()
        payment_method = PaymentMethod.objects.create(id=payment_method_id, name="Cash")
        table = Table.objects.create(id=order_id, number=12)
        waiter = Waiter.objects.create(id=order_id, name="John")
        order = Order.objects.create(id=order_id, waiter=waiter, table=table)
        payment = Payment.objects.create(
            id=payment_id, payment_method=payment_method, order=order, amount=100
        )

        delete_payment_command.send(sender=None, payment_id=payment_id)
        self.assertIsNone(Payment.objects.filter(id=payment_id).first())

    def test_create_order_command(self):
        order_id = uuid4()
        table_id = uuid4()
        waiter_id = uuid4()
        menu_item_id = uuid4()

        MenuItem.objects.create(id=menu_item_id, name="Pizza", price=100)
        Table.objects.create(id=table_id, number=12)
        Waiter.objects.create(id=waiter_id, name="John")

        order_items = [
            OrderItemWriteDto(
                menu_item_id=menu_item_id,
                quantity=1,
            )
        ]

        create_order_command.send(
            sender=None,
            order_id=order_id,
            table_id=table_id,
            waiter_id=waiter_id,
            order_items=order_items,
        )

        self.assertIsNotNone(Order.objects.get(id=order_id))

    def test_delete_order_command(self):
        order_id = uuid4()
        table_id = uuid4()
        waiter_id = uuid4()
        menu_item_id = uuid4()

        menu_item = MenuItem.objects.create(id=menu_item_id, name="Pizza", price=100)
        table = Table.objects.create(id=table_id, number=12)
        waiter = Waiter.objects.create(id=waiter_id, name="John")
        order = Order.objects.create(id=order_id, waiter=waiter, table=table)
        OrderItem.objects.create(
            id=uuid4(), menu_item=menu_item, quantity=1, order=order
        )

        delete_order_command.send(sender=None, order_id=order_id)
        self.assertIsNone(Order.objects.filter(id=order_id).first())


class QueryTestCases(TestCase):
    def test_get_order_total(self):
        waiter = Waiter.objects.create(name="John")
        table = Table.objects.create(number=1)
        order = Order.objects.create(id=uuid4(), waiter=waiter, table=table)
        OrderItem.objects.create(
            id=uuid4(),
            order=order,
            menu_item=MenuItem.objects.create(price=10, name="Pizza"),
            quantity=2,
        )
        OrderItem.objects.create(
            id=uuid4(),
            order=order,
            menu_item=MenuItem.objects.create(price=20, name="Pasta"),
            quantity=1,
        )
        self.assertEqual(get_order_total(order), 40)

    def test_get_orders_with_order_items(self):
        waiter = Waiter.objects.create(name="John")
        table = Table.objects.create(number=1)
        order = Order.objects.create(id=uuid4(), waiter=waiter, table=table)
        OrderItem.objects.create(
            id=uuid4(),
            order=order,
            menu_item=MenuItem.objects.create(price=10, name="Pizza"),
            quantity=2,
        )
        OrderItem.objects.create(
            id=uuid4(),
            order=order,
            menu_item=MenuItem.objects.create(price=20, name="Pasta"),
            quantity=1,
        )

        created_order = get_orders_with_order_items()

        self.assertEqual(created_order.count(), 1)
        self.assertEqual(created_order.first().order_items.count(), 2)

    def test_get_orders(self):
        waiter = Waiter.objects.create(name="John")
        table = Table.objects.create(number=1)
        Order.objects.create(id=uuid4(), waiter=waiter, table=table)
        Order.objects.create(id=uuid4(), waiter=waiter, table=table)

        created_orders = get_orders()

        self.assertEqual(len(created_orders), 2)

    def test_get_order(self):
        waiter = Waiter.objects.create(name="John")
        table = Table.objects.create(number=1)
        order_id = uuid4()
        order = Order.objects.create(id=order_id, waiter=waiter, table=table)
        OrderItem.objects.create(
            id=uuid4(),
            order=order,
            menu_item=MenuItem.objects.create(price=10, name="Pizza"),
            quantity=2,
        )
        OrderItem.objects.create(
            id=uuid4(),
            order=order,
            menu_item=MenuItem.objects.create(price=20, name="Pasta"),
            quantity=1,
        )

        self.assertEqual(get_order(order_id), order)

    def test_get_table(self):
        table = Table.objects.create(number=1)
        self.assertEqual(get_table(table.id), table)

    def test_get_tables(self):
        Table.objects.create(number=1)
        Table.objects.create(number=2)
        self.assertEqual(len(get_tables()), 2)

    def test_get_payment_method(self):
        payment_method = PaymentMethod.objects.create(name="Cash")
        self.assertEqual(get_payment_method(payment_method.id), payment_method)

    def test_get_payment_methods(self):
        PaymentMethod.objects.create(name="Cash")
        PaymentMethod.objects.create(name="Credit Card")
        self.assertEqual(len(get_payment_methods()), 2)

    def test_get_payment(self):
        payment_method = PaymentMethod.objects.create(name="Cash")
        table = Table.objects.create(number=1)
        order = Order.objects.create(
            id=uuid4(), waiter=Waiter.objects.create(name="John"), table=table
        )
        payment_method = PaymentMethod.objects.create(name="Cash")
        payment = Payment.objects.create_payment(
            id=uuid4(), order_id=order.id, payment_method=payment_method, amount=100
        )
        self.assertEqual(get_payment(order.id), payment)

    def test_get_order_add_total(self):
        waiter = Waiter.objects.create(name="John")
        table = Table.objects.create(number=1)
        order_id = uuid4()
        order = Order.objects.create(id=order_id, waiter=waiter, table=table)

        OrderItem.objects.create(
            id=uuid4(),
            order=order,
            menu_item=MenuItem.objects.create(price=10, name="Pizza"),
            quantity=2,
        )
        OrderItem.objects.create(
            id=uuid4(),
            order=order,
            menu_item=MenuItem.objects.create(price=20, name="Pasta"),
            quantity=1,
        )
        self.assertEqual(get_order_add_total(order).total, 40)
