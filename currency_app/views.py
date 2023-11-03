# 3rd-party
from rest_framework import generics

# Local
from .models import Currency
from .serializers import CurrencySerializer


class CurrencyListView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
