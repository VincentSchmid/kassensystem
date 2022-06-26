from django.db import models
from domain.product_catalogue.models import MenuItem


class Table(models.Model):
    number = models.IntegerField()


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)

class Order(models.Model):
    menu_items = models.ManyToManyField(MenuItem, blank=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, null=True)
    total = models.IntegerField(default=0)

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_method = models.OneToOneField(PaymentMethod, on_delete=models.PROTECT)
