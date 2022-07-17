from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import WaiterViewSet, ManagerViewSet


router = SimpleRouter()

router.register(r"waiter", WaiterViewSet, basename="waiter")
router.register(r"manager", ManagerViewSet, basename="manager")

urlpatterns = router.urls
