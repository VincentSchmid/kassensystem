from django.test import TestCase
from core.settings import Groups
from domain.employee.models import Waiter, Manager
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


class EmployeeTestCase(TestCase):
    def setUp(self):
        Group.objects.create(name=Groups.WAITER.value)
        Group.objects.create(name=Groups.MANAGER.value)
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')

    def test_should_create_manager_when_user_is_assigned_as_manager(self):
        user = self.user
        user.groups.add(Group.objects.get(name=Groups.MANAGER.value))
        user.save()
        manager = Manager.objects.get(user=user)
        self.assertEqual(manager.user, user)

    def test_when_user_is_not_assigned_as_manager_then_manager_should_not_be_created(self):
        user = self.user
        manager = Manager.objects.filter(user=user)
        self.assertFalse(manager.exists())

    def test_when_user_is_removed_from_Manager_is_removed(self):
        user = self.user
        user.groups.add(Group.objects.get(name=Groups.MANAGER.value))
        user.save()
        manager = Manager.objects.get(user=user)
        user.groups.remove(Group.objects.get(name=Groups.MANAGER.value))
        user.save()
        self.assertFalse(Manager.objects.filter(user=user).exists())

    def test_should_create_waiter_when_user_is_assigned_as_waiter(self):
        user = self.user
        user.groups.add(Group.objects.get(name=Groups.WAITER.value))
        user.save()
        waiter = Waiter.objects.get(user=user)
        self.assertEqual(waiter.user, user)

    def test_when_user_is_not_assigned_as_waiter_then_waiter_should_not_be_created(self):
        user = self.user
        waiter = Waiter.objects.filter(user=user)
        self.assertFalse(waiter.exists())

    def test_when_user_is_removed_from_Waiter_is_removed(self):
        user = self.user
        user.groups.add(Group.objects.get(name=Groups.WAITER.value))
        user.save()
        waiter = Waiter.objects.get(user=user)
        user.groups.remove(Group.objects.get(name=Groups.WAITER.value))
        user.save()
        self.assertFalse(Waiter.objects.filter(user=user).exists())
