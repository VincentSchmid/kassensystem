from rest_framework import authentication, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OrderSerializer
from .models import Order


# Order
class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes =  [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
