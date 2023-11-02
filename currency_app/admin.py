from django.contrib import admin

from currency_app.models import Currency, ExchangeRate


# Register your models here.
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):  # noqa D101
    pass


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):  # noqa D101
    pass
