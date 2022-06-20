from rest_framework import authentication, permissions
from .serializers import OrderSerializer, OrderWriteSerializer
from .models import Order
from rest_framework import viewsets

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def get_serializer_class(self):
        if self.action == "create":
            return OrderWriteSerializer
        return OrderSerializer
