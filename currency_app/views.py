from rest_framework import generics
from .models import Currency
from .serializers import CurrencyWithExchangeRateSerializer


class CurrencyWithExchangeRateListView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencyWithExchangeRateSerializer
