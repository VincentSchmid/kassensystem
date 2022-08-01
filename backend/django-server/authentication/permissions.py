from django.http import HttpRequest
from ninja_extra import api_controller
from rest_framework import permissions

from ninja_extra.controllers import ControllerBase
from ninja_extra.permissions import BasePermission


class RestrictiveDjangoModelPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        "OPTIONS": [],
        "HEAD": [],
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }


class IsStaffEditorPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            return True

        return False


class ModelPermission(BasePermission):
    def has_permission(self, request: HttpRequest, controller: api_controller):
        app_label = controller.app_label
        model_name = controller.model_name
        perms_map = {
            "OPTIONS": [],
            "HEAD": [],
            "GET": [f"{app_label}.view_{model_name}"],
            "POST": [f"{app_label}.add_{model_name}"],
            "PUT": [f"{app_label}.change_{model_name}"],
            "PATCH": [f"{app_label}.change_{model_name}"],
            "DELETE": [f"{app_label}.delete_{model_name}"],
        }

        return request.user.has_perms(perms_map[request.method])
