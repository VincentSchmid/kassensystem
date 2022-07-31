from typing import List
from uuid import UUID

from domain.employee.models import Waiter, Manager


def get_waiter(id: UUID) -> Waiter:
    return Waiter.objects.get(id=id)


def get_waiter_by_user_id(user_id: UUID) -> Waiter:
    return Waiter.objects.get(user__id=user_id)


def waiter_by_user_id_exists(user_id: UUID) -> bool:
    return Waiter.objects.filter(user__id=user_id).exists()


def get_waiters() -> List[Waiter]:
    return Waiter.objects.all()


def get_manager(id: UUID) -> Manager:
    return Manager.objects.get(id=id)


def get_manager_by_user_id(user_id: UUID) -> Manager:
    return Manager.objects.get(user__id=user_id)


def manager_by_user_id_exists(user_id: UUID) -> bool:
    return Manager.objects.filter(user__id=user_id).exists()


def get_managers() -> List[Manager]:
    return Manager.objects.all()
