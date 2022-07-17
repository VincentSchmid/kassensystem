from requests import Response
from rest_framework import viewsets, mixins, generics
from .serializers import (
    OrderReadSerializer,
    OrderWriteSerializer,
    OrderItemReadSerializer,
    OrderItemWriteSerializer,
    TableSerializer,
    PaymentMethodSerializer,
    PaymentReadSerializer,
    PaymentWriteSerializer,
)
from domain.pos.models import Order, Table, Payment, PaymentMethod, OrderItem


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    http_method_names = ["get", "post", "delete"]


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    http_method_names = ["get", "post", "delete"]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    
    def get_serializer_class(self):
        if self.action == "create":
            return OrderItemWriteSerializer
        return OrderItemReadSerializer


class OrderViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "create":
            return OrderWriteSerializer
        return OrderReadSerializer

    def get_queryset(self):
        if self.action == "list":
            return Order.objects.prefetch_related("order_items")
        return Order.objects.all()


class PaymentView(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView
):
    queryset = Payment.objects.all()
    order_param = "order_id"

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PaymentWriteSerializer
        return PaymentReadSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        order_id = self.kwargs[self.order_param]
        order = Order.objects.get(id=order_id)
        serializer.save(order=order)

    def get_object(self):
        order_id = self.kwargs[self.order_param]
        order = Order.objects.get(id=order_id)
        return self.queryset.filter(order=order).first()
