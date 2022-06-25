from rest_framework import authentication, permissions
from .serializers import (
    OrderReadSerializer,
    OrderWriteSerializer,
    TableSerializer,
    PaymentMethodSerializer,
    PaymentReadSerializer,
    PaymentWriteSerializer,
)
from .models import Order, Table, Payment, PaymentMethod
from rest_framework import viewsets


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = TableSerializer


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = PaymentMethodSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def get_serializer_class(self):
        if self.action == "create":
            return OrderWriteSerializer
        return OrderReadSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def get_serializer_class(self):
        if self.action == "create":
            return PaymentWriteSerializer
        return PaymentReadSerializer

    def get_queryset(self, *args, **kwargs):
        order_id = self.kwargs['order_pk']
        order = Order.objects.get(id=order_id)

        return self.queryset.filter(order=order)

    def perform_create(self, serializer):
        order_id = self.kwargs['order_pk']
        order = Order.objects.get(id=order_id)
        serializer.save(order=order)
