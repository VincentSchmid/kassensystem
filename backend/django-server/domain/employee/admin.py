from django.contrib import admin
from domain.employee.models import Waiter, Manager


@admin.register(Waiter)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    list_per_page = 20

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Manager)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    list_per_page = 20

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
