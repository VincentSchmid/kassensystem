from django.http import HttpRequest
from ninja_extra import api_controller
from ninja_extra.permissions import BasePermission


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
