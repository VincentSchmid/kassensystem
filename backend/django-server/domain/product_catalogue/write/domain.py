from eventsourcing.domain import Aggregate, event


class SalesTax(Aggregate):
    @event("Created")
    def __init__(self, sales_tax_id, name, rate):
        self.sales_tax_id = sales_tax_id
        self.name = name
        self.rate = rate

    @event("RateChanged")
    def change_rate(self, rate):
        self.rate = rate


class Category(Aggregate):
    @event("Created")
    def __init__(self, id, name):
        self.id = id
        self.name = name
