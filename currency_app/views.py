from rest_framework import generics
from .models import Currency
from .serializers import CurrencySerializer


class CurrencyListView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
