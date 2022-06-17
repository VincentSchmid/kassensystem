from rest_framework import authentication, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuItemSerializer, CategorySerializer, SalesTaxSerializer
from .models import MenuItem, Category, SalesTax


# Sales Tax
class SalesTaxListCreateView(ListCreateAPIView):
    queryset = SalesTax.objects.all()
    serializer_class = SalesTaxSerializer
    authentication_classes =  [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class SalesTaxRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SalesTax.objects.all()
    serializer_class = SalesTaxSerializer
    authentication_classes =  [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


# Category
class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes =  [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes =  [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


# Menu Item
class MenuItemListCreateView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    authentication_classes =  [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class MenuItemRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    authentication_classes =  [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
