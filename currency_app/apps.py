from django.apps import AppConfig


class CurrencyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency_app'

    def ready(self):
        import currency_app.signals
