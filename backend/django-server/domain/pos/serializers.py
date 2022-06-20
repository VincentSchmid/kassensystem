from rest_framework import serializers
from .models import Order
from domain.product_catalogue.models import MenuItem
from domain.product_catalogue.serializers import MenuItemSerializer


# Oder serializer
class OrderReadSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "menu_items")


class OrderWriteSerializer(serializers.ModelSerializer):
    menu_items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MenuItem.objects.all(), write_only=True
    )

    class Meta:
        model = Order
        fields = ("id", "menu_items")
