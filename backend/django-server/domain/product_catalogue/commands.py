from uuid import UUID
from django.dispatch import Signal, receiver
from .models import SalesTax, Category, MenuItem


create_sales_tax_command = Signal()
delete_sales_tax_command = Signal()

create_category_command = Signal()
delete_category_command = Signal()

create_menu_item_command = Signal()
delete_menu_item_command = Signal()


@receiver(create_sales_tax_command)
def handle_create_sales_tax(sender, signal, **kwargs):
    SalesTax.objects.create(**kwargs)


@receiver(delete_sales_tax_command)
def handle_delete_sales_tax(sender, signal, **kwargs):
    sales_tax = SalesTax.objects.get(**kwargs)
    sales_tax.delete()


@receiver(create_category_command)
def handle_create_category(sender, signal, **kwargs):
    Category.objects.create(**kwargs)


@receiver(delete_category_command)
def handle_delete_category(sender, signal, **kwargs):
    category = Category.objects.get(**kwargs)
    category.delete()


@receiver(create_menu_item_command)
def handle_create_menu_item(sender, signal, category_id: UUID, **kwargs):
    category = Category.objects.get(id=category_id)
    MenuItem.objects.create(category=category, **kwargs)


@receiver(delete_menu_item_command)
def handle_delete_menu_item(sender, signal, **kwargs):
    menu_item = MenuItem.objects.get(**kwargs)
    menu_item.delete()
