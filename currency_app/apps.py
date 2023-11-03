"""Apps.py files."""
# Django
from django.apps import AppConfig


class CurrencyAppConfig(AppConfig):  # noqa D101
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency_app'

    def ready(self):  # noqa D102
        # Project
        import currency_app.signals  # noqa F401
