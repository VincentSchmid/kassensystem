from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

router.register(r"menu-items", MenuItemViewSet, basename="menu-item")

urlpatterns = [
    path(r"", include(router.urls)),
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
    )
]
