from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuItemSerializer, CategorySerializer, SalesTaxSerializer
from .models import MenuItem, Category, SalesTax


# Sales Tax
class SalesTaxListCreateView(ListCreateAPIView):
    queryset = SalesTax.objects.all()
    serializer_class = SalesTaxSerializer


class SalesTaxRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SalesTax.objects.all()
    serializer_class = SalesTaxSerializer


# Category
class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Menu Item
class MenuItemListCreateView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
