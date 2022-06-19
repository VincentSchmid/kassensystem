from rest_framework import serializers
from .models import Order
from domain.product_catalogue.serializers import MenuItemSerializer

from drf_writable_nested import WritableNestedModelSerializer


# Oder serializer
class OrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ('id', 'menu_items')

class OrderWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'menu_items')
