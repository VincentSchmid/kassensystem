from uuid import uuid4

from django.test import TestCase
from .commands import (
    create_waiter_command,
    delete_waiter_command,
    delete_waiter_by_user_id_command,
    create_manager_command,
    delete_manager_command,
    delete_manager_by_user_id_command,
)
from .queries import (
    get_waiter,
    get_waiter_by_user_id,
    waiter_by_user_id_exists,
    get_waiters,
    get_manager,
    get_managers,
    get_manager_by_user_id,
    manager_by_user_id_exists,
)
from django.contrib.auth import get_user_model
from .models import Waiter, Manager


User = get_user_model()


class EmployeeCommandTestCase(TestCase):
    user: User

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")

    def test_create_waiter_command(self):
        waiter_id = uuid4()
        create_waiter_command.send(
            sender=self, id=waiter_id, user_id=self.user.id, name=self.user.username
        )

        assert Waiter.objects.filter(id=waiter_id).exists()

    def test_delete_waiter_command(self):
        waiter_id = uuid4()
        Waiter.objects.create(id=waiter_id, user_id=self.user.id)
        delete_waiter_command.send(sender=self, id=waiter_id)

        assert not Waiter.objects.filter(id=waiter_id).exists()

    def test_delete_waiter_by_user_id_command(self):
        waiter_id = uuid4()
        Waiter.objects.create(id=waiter_id, user_id=self.user.id)
        delete_waiter_by_user_id_command.send(sender=self, user_id=self.user.id)

        assert not Waiter.objects.filter(id=waiter_id).exists()

    def test_create_manager_command(self):
        manager_id = uuid4()
        create_manager_command.send(
            sender=self, id=manager_id, user_id=self.user.id, name=self.user.username
        )

        assert Manager.objects.filter(id=manager_id).exists()

    def test_delete_manager_command(self):
        manager_id = uuid4()
        Manager.objects.create(id=manager_id, user_id=self.user.id)
        delete_manager_command.send(sender=self, id=manager_id)

        assert not Manager.objects.filter(id=manager_id).exists()

    def test_delete_manager_by_user_id_command(self):
        manager_id = uuid4()
        Manager.objects.create(id=manager_id, user_id=self.user.id)
        delete_manager_by_user_id_command.send(sender=self, user_id=self.user.id)

        assert not Manager.objects.filter(id=manager_id).exists()


class EmployeeQueryTestCase(TestCase):
    user: User

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")

    def test_get_waiter(self):
        waiter_id = uuid4()
        Waiter.objects.create(id=waiter_id, user_id=self.user.id)

        waiter = get_waiter(id=waiter_id)

        assert waiter.id == waiter_id

    def test_get_waiter_by_user_id(self):
        waiter_id = uuid4()
        Waiter.objects.create(id=waiter_id, user_id=self.user.id)
        waiter = get_waiter_by_user_id(user_id=self.user.id)

        assert waiter.id == waiter_id

    def test_waiter_by_user_id_exists(self):
        waiter_id = uuid4()
        Waiter.objects.create(id=waiter_id, user_id=self.user.id)

        assert waiter_by_user_id_exists(user_id=self.user.id)

    def test_get_waiters(self):
        waiter_id = uuid4()
        Waiter.objects.create(id=waiter_id, user_id=self.user.id)
        waiters = get_waiters()

        assert waiter_id in [waiter.id for waiter in waiters]

    def test_get_manager(self):
        manager_id = uuid4()
        Manager.objects.create(id=manager_id, user_id=self.user.id)
        manager = get_manager(id=manager_id)

        assert manager.id == manager_id

    def test_get_manager_by_user_id(self):
        manager_id = uuid4()
        Manager.objects.create(id=manager_id, user_id=self.user.id)
        manager = get_manager_by_user_id(user_id=self.user.id)

        assert manager.id == manager_id

    def test_manager_by_user_id_exists(self):
        manager_id = uuid4()
        Manager.objects.create(id=manager_id, user_id=self.user.id)

        assert manager_by_user_id_exists(user_id=self.user.id)

    def test_get_manager_by_user_id_not_exists(self):
        manager_id = uuid4()
        Manager.objects.create(id=manager_id, user_id=self.user.id)
        manager = get_manager_by_user_id(user_id=uuid4())

        assert manager is None

    def test_get_managers(self):
        manager_id = uuid4()
        Manager.objects.create(id=manager_id, user_id=self.user.id)
        managers = get_managers()

        assert manager_id in [manager.id for manager in managers]
