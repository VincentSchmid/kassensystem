from rest_framework import serializers
from .models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    """
    Serializer for MenuItem model
    """
    class Meta:
        model = MenuItem
        fields = ('id', 'name', 'description', 'price')
