from .views import OrderViewSet, TableViewSet, PaymentMethodViewSet, PaymentView
from rest_framework.routers import SimpleRouter
from django.urls import path, include


router = SimpleRouter()

router.register(r"orders", OrderViewSet, basename="order")
router.register(r"tables", TableViewSet, basename="table")
router.register(r"payment-methods", PaymentMethodViewSet, basename="payment_method")

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"orders/<int:order_id>/payment/", PaymentView.as_view(), name="payment")
]
