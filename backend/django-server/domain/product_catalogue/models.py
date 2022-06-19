from django.db import models


class SalesTax(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=4, decimal_places=2)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
