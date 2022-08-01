from django.contrib.auth.models import Group
from core.settings import Groups
from django.dispatch import receiver
from django.db.models.signals import m2m_changed

from domain.employee.commands import (
    create_waiter_command,
    create_manager_command,
    delete_waiter_by_user_id_command,
    delete_manager_by_user_id_command,
)
from domain.employee.queries import (
    waiter_by_user_id_exists,
    manager_by_user_id_exists,
)


@receiver(m2m_changed)
def signal_handler_when_user_is_added_or_removed_from_group(
    action, instance, pk_set, model, **kwargs
):
    for pk in pk_set:
        if model == Group:
            if action == "post_add":
                group = Group.objects.get(id=pk)
                if group.name == Groups.WAITER.value:
                    create_waiter_command.send(
                        sender=None, user_id=instance.id, name=instance.username
                    )
                elif group.name == Groups.MANAGER.value:
                    create_manager_command.send(
                        sender=None, user_id=instance.id, name=instance.username
                    )

            if action == "pre_remove":
                group = Group.objects.get(id=pk)
                if group.name == Groups.WAITER.value and waiter_by_user_id_exists(
                    instance.id
                ):
                    delete_waiter_by_user_id_command.send(
                        sender=None, user_id=instance.id
                    )
                elif group.name == Groups.MANAGER.value and manager_by_user_id_exists(
                    instance.id
                ):
                    delete_manager_by_user_id_command.send(
                        sender=None, user_id=instance.id
                    )
