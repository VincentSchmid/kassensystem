from uuid import uuid4

from django.db import models
from django.contrib.postgres.fields import CICharField, CIEmailField
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        # if email was passed in extra_fields, normalize it
        if "email" in extra_fields:
            extra_fields["email"] = self.normalize_email(extra_fields["email"])

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username_validator = ASCIIUsernameValidator()

    username = CICharField(
        verbose_name="username",
        max_length=30,
        unique=True,
        validators=[username_validator],
        help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={
            "unique": "A user with that username already exists.",
            "invalid": "Username may only contain letters, digits and @/./+/-/_ characters.",
        },
    )
    first_name = models.CharField(verbose_name="first name", max_length=30, blank=True)
    last_name = models.CharField(verbose_name="last name", max_length=30, blank=True)
    email = CIEmailField(
        verbose_name="email",
        max_length=60,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    objects = UserManager()

    def __str__(self):
        return self.username
