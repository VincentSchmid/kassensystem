from rest_framework import authentication, permissions
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveDestroyAPIView
from .serializers import OrderSerializer, OrderWriteSerializer
from .models import Order


# Order
class OderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes =  [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderWriteSerializer
    authentication_classes =  [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class OrderRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes =  [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class OrderUpdateDeleteView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderWriteSerializer
    authentication_classes =  [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
