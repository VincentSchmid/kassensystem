from rest_framework import serializers
from .models import MenuItem, Category, SalesTax

from drf_writable_nested import WritableNestedModelSerializer


# Sales Tax
class SalesTaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTax
        fields = ("id", "name", "rate")


# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


# Menu Item
class MenuItemSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ("id", "name", "price", "category")
