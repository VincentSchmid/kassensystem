from django.db import models
from domain.product_catalogue.models import MenuItem
from domain.employee.models import Waiter


class Table(models.Model):
    number = models.IntegerField()


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, null=True)
    waiter = models.ForeignKey(Waiter, on_delete=models.SET_NULL, null=True)

    @property
    def total(self):
        return sum([item.price for item in self.menu_items.all()])


class OrderItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')

    def __str__(self):
        return self.menu_item.name


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_method = models.OneToOneField(PaymentMethod, on_delete=models.PROTECT)
