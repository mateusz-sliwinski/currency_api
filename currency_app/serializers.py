# 3rd-party
from rest_framework import serializers

# Local
from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'
