from .views import OrderViewSet, PaymentViewSet, TableViewSet, PaymentMethodViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter
from django.urls import path, include


router = SimpleRouter()

router.register(r"orders", OrderViewSet, basename="order")
orders_router = NestedSimpleRouter(router, r"orders", lookup="order")
orders_router.register(r"payments", PaymentViewSet, basename="order-payment")

router.register(r"tables", TableViewSet, basename="table")
router.register(r"payment-methods", PaymentMethodViewSet, basename="payment_method")

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(orders_router.urls))
]
