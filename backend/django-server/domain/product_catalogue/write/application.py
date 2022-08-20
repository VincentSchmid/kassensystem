from functools import singledispatchmethod
from eventsourcing.system import ProcessApplication
from eventsourcing.application import Application

from domain.product_catalogue.signals import sales_tax_created, sales_tax_rate_changed
from .domain import SalesTax, Category


class ProductCatalogue(Application):
    def create_sales_tax(self, id, name, rate):
        salesTax = SalesTax(sales_tax_id=id, name=name, rate=rate)
        self.save(salesTax)
        return salesTax.id

    def change_sales_tax_rate(self, id, rate):
        salesTax = self.get(SalesTax, id)
        salesTax.change_rate(rate)
        self.save(salesTax)

    def create_category(self, id, name):
        category = Category(id=id, name=name)
        self.save(category)
        return category.id

class ProductCatalogueProcess(ProcessApplication):
    @singledispatchmethod
    def policy(self, domain_event, _):
        """Default policy"""

    @policy.register(SalesTax.Created)
    def _(self, domain_event, _):
        sales_tax_created.send(sender=None, domain_event=domain_event)

    @policy.register(SalesTax.RateChanged)
    def _(self, domain_event, _):
        sales_tax_rate_changed.send(sender=None, domain_event=domain_event)
