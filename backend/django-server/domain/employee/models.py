from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.models import Group


User = get_user_model()

class Waiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Waiter'
        verbose_name_plural = 'Waiters'

    def __str__(self):
        return self.name


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

    def __str__(self):
        return self.name
