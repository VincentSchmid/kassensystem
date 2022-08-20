from enum import Enum
from uuid import UUID, uuid4

from django.db import models

from domain.product_catalogue.read.models import MenuItem
from domain.employee.models import Waiter


class OrderState(Enum):
    PAID = "paid"
    UNPAID = "unpaid"


class Table(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    number = models.IntegerField()


class PaymentMethod(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)


class OrderManager(models.Manager):
    def create(self, id: UUID, waiter: Waiter, table: Table):
        return self.get_queryset().create(
            id=id, waiter=waiter, table=table, status=OrderState.UNPAID.name
        )

    def add_payment(self, payment):
        payment.order.status = OrderState.PAID.name
        payment.order.save()


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, null=True)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)

    objects = OrderManager()


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )

    def __str__(self):
        return self.menu_item.name


class PaymentManager(models.Manager):
    def create_payment(
        self, id: UUID, order_id: UUID, amount: float, payment_method: PaymentMethod
    ):
        order = Order.objects.get(id=order_id)
        payment = self.get_queryset().create(
            id=id, order=order, amount=amount, payment_method=payment_method
        )
        return payment

    def get_payment(self, order_id: UUID):
        return super().get_queryset().filter(order__id=order_id).first()


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)

    objects = PaymentManager()
