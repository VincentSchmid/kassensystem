from uuid import uuid4

from django.test import TestCase

from .models import SalesTax, Category, MenuItem
from .queries import (
    get_sales_tax,
    get_sales_taxes,
    get_category,
    get_categories,
    get_menu_item,
    get_menu_items,
)


class QueryProductCatalogueTestCases(TestCase):
    def test_get_sales_tax(self):
        sales_tax_id = uuid4()
        SalesTax.objects.create(id=sales_tax_id, rate=0.1)
        self.assertIsNotNone(get_sales_tax(sales_tax_id))

    def test_get_sales_taxes(self):
        sales_tax_id = uuid4()
        SalesTax.objects.create(id=sales_tax_id, rate=0.1)
        self.assertIsNotNone(get_sales_taxes())
        self.assertEqual(1, len(get_sales_taxes()))

    def test_get_category(self):
        category_id = uuid4()
        Category.objects.create(id=category_id, name="Test Category")
        self.assertIsNotNone(get_category(category_id))

    def test_get_categories(self):
        category_id = uuid4()
        Category.objects.create(id=category_id, name="Test Category")
        self.assertIsNotNone(get_categories())
        self.assertEqual(1, len(get_categories()))

    def test_get_menu_item(self):
        category_id = uuid4()
        Category.objects.create(id=category_id, name="Test Category")
        menu_item_id = uuid4()
        MenuItem.objects.create(
            id=menu_item_id, category_id=category_id, name="Menu Item", price=10
        )
        self.assertIsNotNone(get_menu_item(menu_item_id))

    def test_get_menu_items(self):
        category_id = uuid4()
        Category.objects.create(id=category_id, name="Test Category")
        menu_item_id = uuid4()
        MenuItem.objects.create(
            id=menu_item_id, category_id=category_id, name="Menu Item", price=10
        )
        self.assertIsNotNone(get_menu_items())
        self.assertEqual(1, len(get_menu_items()))
