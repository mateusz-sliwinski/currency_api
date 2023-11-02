"""Urls.py Files."""
# Django
from django.urls import path
from currency_app.views import  CurrencyWithExchangeRateListView

urlpatterns = [
    path('currency/', CurrencyWithExchangeRateListView.as_view(), name='currency'),

]
