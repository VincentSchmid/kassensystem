from django.test import TestCase

from domain.product_catalogue.models import MenuItem
from domain.employee.models import Waiter
from domain.pos.models import Order, OrderItem, Table
from domain.pos.queries import get_order_total, get_orders_with_order_items


class QueryTestCases(TestCase):
    def test_get_order_total(self):
        waiter = Waiter.objects.create(name="John")
        table = Table.objects.create(number=1)
        order = Order.objects.create(waiter=waiter, table=table)
        OrderItem.objects.create(
            order=order,
            menu_item=MenuItem.objects.create(price=10, name="Pizza"),
            quantity=2,
        )
        OrderItem.objects.create(
            order=order,
            menu_item=MenuItem.objects.create(price=20, name="Pasta"),
            quantity=1,
        )
        self.assertEqual(get_order_total(order), 40)

    def test_get_orders_with_order_items(self):
        waiter = Waiter.objects.create(name="John")
        table = Table.objects.create(number=1)
        order = Order.objects.create(waiter=waiter, table=table)
        OrderItem.objects.create(
            order=order,
            menu_item=MenuItem.objects.create(price=10, name="Pizza"),
            quantity=2,
        )
        OrderItem.objects.create(
            order=order,
            menu_item=MenuItem.objects.create(price=20, name="Pasta"),
            quantity=1,
        )
        self.assertEqual(get_orders_with_order_items().count(), 1)
        self.assertEqual(get_orders_with_order_items().first().order_items.count(), 2)
        self.assertEqual(
            get_orders_with_order_items().first().order_items.first().menu_item.price,
            10,
        )
        self.assertEqual(
            get_orders_with_order_items().first().order_items.last().menu_item.price, 20
        )
