from django.dispatch import receiver
from domain.product_catalogue.signals import sales_tax_created, sales_tax_rate_changed
from .models import SalesTax


@receiver(sales_tax_created)
def handle_create_sales_tax(sender, signal, domain_event, **kwargs):
    SalesTax.objects.get_or_create(id=domain_event.sales_tax_id, name=domain_event.name, rate=domain_event.rate)

@receiver(sales_tax_rate_changed)
def handle_update_sales_tax(sender, signal, domain_event, **kwargs):
    SalesTax.objects.filter(id=domain_event.id).update(rate=domain_event.rate)
