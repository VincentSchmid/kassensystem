import logging

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.conf import settings


class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):
        for group, permissions in settings.GROUPS.items():
            new_group, created = Group.objects.get_or_create(name=group)
            if created:
                logging.info("Created group %s" % group)
