from rest_framework import serializers
from .models import Order
from domain.product_catalogue.serializers import MenuItemPublicSerializer


# Oder serializer
class OrderSerializer(serializers.ModelSerializer):
    menu_item = MenuItemPublicSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'menu_item')
