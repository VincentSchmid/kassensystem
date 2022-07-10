from rest_framework import viewsets, mixins, generics
from django.db.models import Sum
from .serializers import (
    OrderReadSerializer,
    OrderWriteSerializer,
    TableSerializer,
    PaymentMethodSerializer,
    PaymentReadSerializer,
    PaymentWriteSerializer,
)
from .models import Order, Table, Payment, PaymentMethod


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    http_method_names = ["get", "post", "delete"]


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    http_method_names = ["get", "post", "delete"]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
        
    def get_serializer_class(self):
        if self.action == "create":
            return OrderWriteSerializer
        return OrderReadSerializer


class PaymentView(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView
):
    queryset = Payment.objects.all()
    order_param = "order_id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PaymentWriteSerializer
        return PaymentReadSerializer

    def perform_create(self, serializer):
        order_id = self.kwargs[self.order_param]
        order = Order.objects.get(id=order_id)
        serializer.save(order=order)

    def get_object(self):
        order_id = self.kwargs[self.order_param]
        order = Order.objects.get(id=order_id)
        return self.queryset.filter(order=order).first()
