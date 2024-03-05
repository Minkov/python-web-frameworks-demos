from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "custom_auth_demos.accounts"

    def ready(self):
        import custom_auth_demos.accounts.signals