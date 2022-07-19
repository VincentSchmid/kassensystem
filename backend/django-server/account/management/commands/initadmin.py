import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--username", "-u")
        parser.add_argument("--email", "-e")
        parser.add_argument("--password", "-p")

    def handle(self, *args, **options):
        username = options["username"]
        email = options["email"]
        password = options["password"]

        if not User.objects.filter(username=username).exists():
            logging.info(f"Creating admin: {username}")
            admin = User.objects.create_superuser(
                email=email, username=username, password=password
            )
            admin.is_active = True
            admin.is_admin = True
            admin.save()
