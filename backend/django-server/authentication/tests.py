from uuid import uuid4
from unittest.mock import MagicMock

from django.test import TransactionTestCase
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import m2m_changed

from domain.employee.commands import (
    create_waiter_command,
    create_manager_command,
    delete_waiter_by_user_id_command,
    delete_manager_by_user_id_command,
)
from domain.employee.models import Waiter, Manager


User = get_user_model()


class SignalTestCase(TransactionTestCase):
    user: User

    def setUp(self) -> None:
        Group.objects.create(name="WAITER")
        Group.objects.create(name="MANAGER")

        self.user = User.objects.create_user(username="test", password="test")

    def test_signal_when_user_is_added_to_group(self):
        mock_func = MagicMock()
        create_waiter_command.connect(mock_func, sender="test")
        self.user.groups.add(Group.objects.get(name="WAITER"))
        self.user.groups.add(Group.objects.get(name="MANAGER"))

        # self.assertEqual(Waiter.objects.filter(user_id=self.user.id).count(), 1)
