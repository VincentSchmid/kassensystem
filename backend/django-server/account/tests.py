from io import StringIO

from django.test import TestCase
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


User = get_user_model()


class AccountTestCase(TestCase):
    def call_command(self, *args, **kwargs):
        out = StringIO()
        call_command(
            "initadmin",
            *args,
            stdout=out,
            stderr=StringIO(),
            **kwargs,
        )
        return out.getvalue()

    def test_write_empty(self):
        self.call_command(
            "--username", "admin", "--email", "admin@admin.com", "--password", "admin"
        )

        new_user = User.objects.get(username="admin")
        self.assertTrue(new_user.is_admin)


class GroupCommandTestCase(AccountTestCase):
    def call_command(self, *args, **kwargs):
        out = StringIO()
        call_command(
            "initgroups",
            *args,
            stdout=out,
            stderr=StringIO(),
            **kwargs,
        )
        return out.getvalue()

    def test_write_empty(self):
        self.call_command()

        waiter_group = Group.objects.get(name="Waiter")
        manager_group = Group.objects.get(name="Manager")

        self.assertIsNotNone(waiter_group)
        self.assertIsNotNone(manager_group)
