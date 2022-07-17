from enum import Enum

from django.db import models
from django.dispatch import receiver

from domain.product_catalogue.models import MenuItem
from domain.employee.models import Waiter
from domain.pos.signals import payment_created


class OrderState(Enum):
    PAID = "paid"
    UNPAID = "unpaid"


class Table(models.Model):
    number = models.IntegerField()


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)


class OrderManager(models.Manager):
    def create(self, waiter:Waiter, table:Table):
        return self.get_queryset().create(waiter=waiter, table=table, status=OrderState.UNPAID.name)

    @receiver(payment_created)
    def set_order_status(sender, payment, **kwargs):
        payment.order.status = OrderState.PAID.name
        payment.order.save()


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, null=True)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)

    objects = OrderManager()


# class OrderItemManager(models.Manager):
#     def create(self, order:Order, menu_item:MenuItem, quantity:int):
#         self.get_queryset().create(order=order, menu_item=menu_item, quantity=quantity)


class OrderItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')

#    objects = OrderItemManager()

    def __str__(self):
        return self.menu_item.name


class PaymentManager(models.Manager):
    def create_payment(self, order_id: int, amount: float, payment_method: PaymentMethod):
        order = Order.objects.get(id=order_id)
        payment = self.get_queryset().create(order=order, amount=amount, payment_method=payment_method)
        payment_created.send(sender=Payment, payment=payment)
        return payment

    def get_payment(self, order_id: int):
        return super().get_queryset().filter(order__id=order_id).first()


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)

    objects = PaymentManager()
