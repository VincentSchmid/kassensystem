from django.db import models
import datetime


class ModifiableEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    valid_from = models.DateTimeField(auto_now_add=True)
    valid_to = models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59))

    class Meta:
        abstract = True
