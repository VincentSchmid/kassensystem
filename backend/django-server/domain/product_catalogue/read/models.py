from uuid import uuid4

from django.db import models
from persistence.models import ModifiableEntity


class SalesTax(ModifiableEntity):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=4, decimal_places=2)


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MenuItem(ModifiableEntity):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

from .events import *
