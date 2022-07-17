from rest_framework import serializers

from domain.employee.models import Waiter
from domain.product_catalogue.models import MenuItem
from domain.product_catalogue.serializers import MenuItemSerializer
from domain.pos.models import Order, Table, Payment, PaymentMethod, OrderItem
from domain.pos.queries import get_order_total


class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ("id", "name")


# Table serializer
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ("id", "number")


# PaymentMethod serializer
class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ("id", "name")


# Payment serializer
class PaymentReadSerializer(serializers.ModelSerializer):
    payment_method = PaymentMethodSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ("id", "amount", "payment_method")


class PaymentWriteSerializer(serializers.ModelSerializer):
    payment_method = serializers.PrimaryKeyRelatedField(
        queryset=PaymentMethod.objects.all(), write_only=True
    )

    class Meta:
        model = Payment
        fields = ("id", "amount", "payment_method")


class OrderItemReadSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ("id", "menu_item", "quantity")


class OrderItemWriteSerializer(serializers.ModelSerializer):
    menu_item = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(), write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ("id", "menu_item", "quantity")


# Oder serializer
class OrderReadSerializer(serializers.ModelSerializer):
    order_items = OrderItemReadSerializer(many=True, read_only=True)
    table = TableSerializer(read_only=True)
    waiter = WaiterSerializer(read_only=True)
    total = serializers.SerializerMethodField("get_total")

    def get_total(self, order):
        return get_order_total(order)

    class Meta:
        model = Order
        fields = ("id", "order_items", "table", "waiter", "status", "total")


class OrderWriteSerializer(serializers.ModelSerializer):
    order_items = OrderItemWriteSerializer(many=True, write_only=True)
    table = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(), write_only=True
    )
    waiter = serializers.PrimaryKeyRelatedField(
        queryset=Waiter.objects.all(), write_only=True
    )

    class Meta:
        model = Order
        fields = ("id", "order_items", "table", "waiter")

    def create(self, validated_data):
        order_items = validated_data.pop("order_items")
        order = Order.objects.create(**validated_data)
        for order_item in order_items:
            OrderItem.objects.create(order=order, **order_item)
        return order
