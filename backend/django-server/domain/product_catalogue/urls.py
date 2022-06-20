from django.urls import path
from .views import *


urlpatterns = [
    path("sales-tax/", SalesTaxListCreateView.as_view(), name="sales-tax-list"),
    path(
        "sales-tax/<int:pk>/",
        SalesTaxRetrieveUpdateDestroyView.as_view(),
        name="sales-tax-detail",
    ),
    path("category/", CategoryListCreateView.as_view(), name="category-list"),
    path(
        "category/<int:pk>/",
        CategoryRetrieveUpdateDestroyView.as_view(),
        name="category-detail",
    ),
    path("menu-item/", MenuItemListCreateView.as_view(), name="menuitem-list"),
    path(
        "menu-item/<int:pk>/",
        MenuItemRetrieveUpdateDestroyView.as_view(),
        name="menuitem-detail",
    ),
]
