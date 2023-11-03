"""Urls.py Files."""
# Django
from django.urls import path

# Project
from currency_app.views import CurrencyListView

urlpatterns = [
    path('currency/', CurrencyListView.as_view(), name='currency'),
]
