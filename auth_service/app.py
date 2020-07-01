from django.apps import AppConfig


class AuthServiceAppConfig(AppConfig):
    name = "auth_service"

    def ready(self):
        from auth_service import signals # pylint: disable=unused-variable
