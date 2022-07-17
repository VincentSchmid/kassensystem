from rest_framework import serializers

from domain.employee.models import Waiter


class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ("id", "name")


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ("id", "name")
