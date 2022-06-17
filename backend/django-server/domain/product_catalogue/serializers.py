from rest_framework import serializers
from .models import MenuItem, Category, SalesTax


# Sales Tax
class SalesTaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTax
        fields = ('id', 'name', 'rate')


# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


# Menu Item
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'name', 'price')


# Menu Item public serializer
class MenuItemPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)
