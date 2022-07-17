from domain.employee.models import Waiter, Manager
from django.contrib.auth.models import Group
from core.settings import Groups
from django.dispatch import receiver
from django.db.models.signals import m2m_changed


@receiver(m2m_changed)
def signal_handler_when_user_is_added_or_removed_from_group(action, instance, pk_set, model, **kwargs):
    for pk in pk_set:
        if model == Group:
            if action == 'post_add':
                group = Group.objects.get(id=pk)
                if group.name == Groups.WAITER.value:
                    waiter, created = Waiter.objects.get_or_create(user=instance, name=instance.username)
                    waiter.save()
                elif group.name == Groups.MANAGER.value:
                    manager, created = Manager.objects.get_or_create(user=instance, name=instance.username)
                    manager.save()

            if action == "pre_remove":
                group = Group.objects.get(id=pk)
                if group.name == Groups.WAITER.value and Waiter.objects.filter(user=instance).exists():
                    waiter = Waiter.objects.get(user=instance)
                    waiter.delete()
                elif group.name == Groups.MANAGER.value and Manager.objects.filter(user=instance).exists():
                    manager = Manager.objects.get(user=instance)
                    manager.delete()
