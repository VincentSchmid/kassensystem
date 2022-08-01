from typing import List
from uuid import UUID

from django.http import HttpResponse
from ninja_extra import api_controller, http_get, http_delete
from ninja_jwt.authentication import JWTAuth

from .dtos import (
    WaiterReadDto,
    ManagerReadDto,
)

from .commands import (
    delete_waiter_command,
    delete_manager_command,
)

from .queries import (
    get_waiter,
    get_waiters,
    get_manager,
    get_managers,
)


@api_controller("/waiters", tags=["Waiters"], auth=JWTAuth())
class WaiterController:
    @http_get("/", response=List[WaiterReadDto])
    def handle_get_waiters(request):
        return get_waiters()

    @http_get("/{waiter_id}", response=WaiterReadDto)
    def handle_get_waiter_detail(request, waiter_id: UUID):
        return get_waiter(waiter_id)

    @http_delete("/{waiter_id}")
    def handle_delete_waiter(request, waiter_id: UUID):
        delete_waiter_command.send(sender=None, id=waiter_id)
        return HttpResponse(status=204)

    @http_get("/", response=List[ManagerReadDto])
    def handle_get_managers(request):
        return get_managers()

    @http_get("/{manager_id}", response=ManagerReadDto)
    def handle_get_manager_detail(request, manager_id: UUID):
        return get_manager(manager_id)

    @http_delete("/{manager_id}")
    def handle_delete_manager(request, manager_id: UUID):
        delete_manager_command.send(sender=None, id=manager_id)
        return HttpResponse(status=204)
