from typing import List
from uuid import UUID

from .models import SalesTax, Category, MenuItem


def get_sales_tax(id: UUID) -> SalesTax:
    return SalesTax.objects.get(id=id)


def get_sales_taxes() -> List[SalesTax]:
    return SalesTax.objects.all()


def get_category(id: UUID) -> Category:
    return Category.objects.get(id=id)


def get_categories() -> List[Category]:
    return Category.objects.all()


def get_menu_item(id: UUID) -> MenuItem:
    return MenuItem.objects.get(id=id)


def get_menu_items() -> List[MenuItem]:
    return MenuItem.objects.all()
