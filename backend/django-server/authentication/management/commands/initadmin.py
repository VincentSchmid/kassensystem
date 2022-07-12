from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        username = settings.ADMIN["USERNAME"]
        email = settings.ADMIN["EMAIL"]
        password = settings.ADMIN["PASSWORD"]

        if not User.objects.filter(username=username).exists():
            print("Creating account for %s (%s)" % (username, email))
            admin = User.objects.create_superuser(
                email=email, username=username, password=password
            )
            admin.is_active = True
            admin.is_admin = True
            admin.save()
