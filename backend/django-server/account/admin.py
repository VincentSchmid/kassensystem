from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    search_fields = [
        "username",
        "first_name",
        "last_name",
    ]
    list_display = (
        "username",
        "first_name",
        "last_name",
    )
    filter_horizontal = ("groups", "user_permissions")
    fieldsets = (
        ("User", {"fields": ("username", "password")}),
        (
            "Personal Information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )


admin.site.register(Account, UserAdmin)
