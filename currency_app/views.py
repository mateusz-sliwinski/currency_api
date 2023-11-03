"""Views.py Files."""
# 3rd-party
from rest_framework import generics

# Local
from .models import Currency
from .serializers import CurrencySerializer


class CurrencyListView(generics.ListAPIView):
    """
    A view for listing Currency objects.

    This view is implemented as a generic ListAPIView and is used
    for retrieving a list of Currency objects
    from the database. It sets the `queryset` to include all
    Currency objects and specifies the `serializer_class`
    for serializing the data.

    Example usage:
    ```
    urlpatterns = [
        path('currency/', CurrencyListView.as_view(), name='currency'),
    ]
    ```

    Attributes:
        queryset: The database query to retrieve a list of Currency objects.
        serializer_class: The serializer class to use for serializing the retrieved data.

    Note:
    To use this view, you should include it in your Django application's URL configuration.
    """

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
