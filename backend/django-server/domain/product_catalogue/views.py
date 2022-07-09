from rest_framework import authentication, permissions, viewsets, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuItemSerializer, CategorySerializer, SalesTaxSerializer
from django.utils import timezone
from rest_framework.response import Response

from .models import MenuItem, Category, SalesTax
from authentication.permissions import IsStaffEditorPermissions


# Sales Tax
class SalesTaxListCreateView(ListCreateAPIView):
    queryset = SalesTax.objects.all()
    serializer_class = SalesTaxSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class SalesTaxRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SalesTax.objects.all()
    serializer_class = SalesTaxSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


# Category
class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


# Menu Item
class MenuItemViewSet(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    authentication_classes = [authentication.SessionAuthentication]
    http_method_names = ["get", "post", "delete", "put"]

    def update(self, request, *args, **kwargs):
        now = timezone.now()
        current = self.get_queryset().get(id=kwargs["pk"])
        current.valid_to = now
        current.save()

        return self.create(request)

    def destroy(self, request, *args, **kwargs):
        now = timezone.now()
        current = self.get_queryset().get(id=kwargs["pk"])
        current.valid_to = now
        current.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = MenuItem.objects.all()

        if self.action == "list":
            return queryset.filter(valid_to__gt=timezone.now())

        return queryset
