from rest_framework import serializers
from .models import Currency, ExchangeRate


class CurrencyWithExchangeRateSerializer(serializers.ModelSerializer):
    exchange_rates = serializers.SerializerMethodField()

    class Meta:
        model = Currency
        fields = '__all__'

    def get_exchange_rates(self, obj):
        rates = ExchangeRate.objects.filter(currency_from=obj)
        return ExchangeRateSerializer(rates, many=True).data


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'
