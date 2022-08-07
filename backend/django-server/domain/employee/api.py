from typing import List
from uuid import UUID

from ninja_extra import api_controller, http_get
from ninja_jwt.authentication import JWTAuth
from authentication.permissions import ModelPermission

from .dtos import (
    WaiterReadDto,
    ManagerReadDto,
)

from .queries import (
    get_waiter,
    get_waiters,
    get_manager,
    get_managers,
)


@api_controller(
    "/waiters", tags=["Waiters"], auth=JWTAuth(), permissions=[ModelPermission]
)
class WaiterController:
    app_label = "employee"
    model_name = "waiter"

    @http_get("/", response=List[WaiterReadDto])
    def handle_get_waiters(self, request):
        return get_waiters()

    @http_get("/{waiter_id}", response=WaiterReadDto)
    def handle_get_waiter_detail(self, request, waiter_id: UUID):
        return get_waiter(waiter_id)


@api_controller(
    "/managers", tags=["Waiters"], auth=JWTAuth(), permissions=[ModelPermission]
)
class ManagerController:
    app_label = "employee"
    model_name = "manager"

    @http_get("/", response=List[ManagerReadDto])
    def handle_get_managers(self, request):
        return get_managers()

    @http_get("/{manager_id}", response=ManagerReadDto)
    def handle_get_manager_detail(self, request, manager_id: UUID):
        return get_manager(manager_id)
