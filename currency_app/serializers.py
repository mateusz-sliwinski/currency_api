"""Serializers.py Files."""
# 3rd-party
from rest_framework import serializers

# Local
from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    """
    Serializer class for the Currency model.

    This serializer is used to convert Currency model instances into
    JSON representations and vice versa.
    It includes all fields from the Currency model in the serialization.

    Example usage:
    ```
    class CurrencyListView(generics.ListAPIView):
        queryset = Currency.objects.all()
        serializer_class = CurrencySerializer
    ```

    Attributes:
        model: The Django model class associated with this serializer.
        fields: A list of field names to include in the serialization.
        In this case, '__all__' includes all fields.
    """

    class Meta:  # noqa D106
        model = Currency
        fields = '__all__'
