from django.db import models
import datetime
from django.utils.timezone import get_current_timezone


class ModifiableEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    valid_from = models.DateTimeField(auto_now_add=True)
    valid_to = models.DateTimeField(
        default=datetime.datetime(
            9999, 12, 31, 23, 59, 59, tzinfo=get_current_timezone()
        )
    )

    class Meta:
        abstract = True
