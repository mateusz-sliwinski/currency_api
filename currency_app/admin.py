# Django
from django.contrib import admin

# 3rd-party
from rangefilter.filters import DateRangeFilter

# Project
from currency_app.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):  # noqa D101
    list_display = [
        'code',
        'date',
        'rate',
    ]
    list_filter = [
        ('date', DateRangeFilter),
    ]
    list_display_links = (
        'code',
    )
    list_editable = [
        'rate',
    ]
    search_fields = [
        'code',
    ]
