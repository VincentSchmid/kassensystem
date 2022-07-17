from rest_framework import viewsets
from .models import Waiter, Manager
from .serializers import WaiterSerializer, ManagerSerializer


class WaiterViewSet(viewsets.ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
    http_method_names = ["get"]


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    http_method_names = ["get"]
