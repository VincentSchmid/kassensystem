from .views import OrderViewSet, PaymentViewSet, TableViewSet, PaymentMethodViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"orders", OrderViewSet, basename="order")
router.register(r"payments", PaymentViewSet, basename="payment")
router.register(r"tables", TableViewSet, basename="table")
router.register(r"payment_methods", PaymentMethodViewSet, basename="payment_method")

urlpatterns = router.urls
