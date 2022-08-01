from uuid import UUID
from django.dispatch import Signal, receiver
from .models import Waiter, Manager

create_waiter_command = Signal()
delete_waiter_command = Signal()
delete_waiter_by_user_id_command = Signal()

create_manager_command = Signal()
delete_manager_command = Signal()
delete_manager_by_user_id_command = Signal()


@receiver(create_waiter_command)
def handle_create_waiter(sender, signal, **kwargs):
    Waiter.objects.get_or_create(**kwargs)


@receiver(delete_waiter_command)
def handle_delete_waiter(sender, signal, **kwargs):
    waiter = Waiter.objects.get(**kwargs)
    waiter.delete()


@receiver(delete_waiter_by_user_id_command)
def handle_delete_waiter_by_user_id(sender, signal, user_id: UUID, **kwargs):
    waiter = Waiter.objects.get(user_id=user_id)
    waiter.delete()


@receiver(create_manager_command)
def handle_create_manager(sender, signal, **kwargs):
    Manager.objects.get_or_create(**kwargs)


@receiver(delete_manager_command)
def handle_delete_manager(sender, signal, **kwargs):
    manager = Manager.objects.get(**kwargs)
    manager.delete()


@receiver(delete_manager_by_user_id_command)
def handle_delete_manager_by_user_id(sender, signal, user_id: UUID, **kwargs):
    manager = Manager.objects.get(user_id=user_id)
    manager.delete()
