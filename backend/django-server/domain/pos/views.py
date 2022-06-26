from rest_framework import authentication, permissions, viewsets, mixins, generics
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


class PaymentView(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView
):
    queryset = Payment.objects.all()
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PaymentWriteSerializer
        return PaymentReadSerializer

    def perform_create(self, serializer):
        order_id = self.kwargs["order_pk"]
        order = Order.objects.get(id=order_id)
        serializer.save(order=order)

    def get_object(self):
        order_id = self.kwargs["order_pk"]
        order = Order.objects.get(id=order_id)
        return self.queryset.get(order=order)
