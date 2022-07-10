from multiprocessing.connection import wait
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order, Table, Payment, PaymentMethod
from domain.product_catalogue.models import MenuItem
from domain.product_catalogue.serializers import MenuItemSerializer


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")

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


# Oder serializer
class OrderReadSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)
    table = TableSerializer(read_only=True)
    waiter = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("id", "menu_items", "table", "waiter", "status", "total")


class OrderWriteSerializer(serializers.ModelSerializer):
    menu_items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MenuItem.objects.all(), write_only=True
    )
    table = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(), write_only=True
    )
    waiter = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True
    )

    class Meta:
        model = Order
        fields = ("id", "menu_items", "table", "waiter", "status")
