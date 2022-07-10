from django.db import models
from domain.product_catalogue.models import MenuItem
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from core.settings import Groups


User = get_user_model()

def validate_is_waiter(user_id):
    user = User.objects.get(id=user_id)
    if not user.groups.filter(name=Groups.WAITER.name).exists():
        raise ValidationError(
            (f"User with id: {user_id} is not a waiter")
        )

class Table(models.Model):
    number = models.IntegerField()


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)


class Order(models.Model):
    menu_items = models.ManyToManyField(MenuItem, blank=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, null=True)
    waiter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, validators=[validate_is_waiter])

    @property
    def total(self):
        return sum([item.price for item in self.menu_items.all()])


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_method = models.OneToOneField(PaymentMethod, on_delete=models.PROTECT)
