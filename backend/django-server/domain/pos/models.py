from django.db import models
from domain.product_catalogue.models import MenuItem


class Order(models.Model):
    menu_items = models.ManyToManyField(MenuItem, blank=True)
