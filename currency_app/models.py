"""Models.py Files."""
# Standard Library
import uuid

# Django
from django.db import models


class UUIDMixin(models.Model):
    """
    A mixin for adding a UUID (Universally Unique Identifier) field as the primary key to a Django model.

    This mixin provides a UUID field named 'id' as the primary key
    for the model, ensuring each record
    has a unique identifier. The 'id' field is automatically generated
    using the uuid4 function from the uuid module.

    Attributes:
        id (uuid.UUID): The UUID field serving as the primary key.

    Meta:
        abstract (bool): Indicates that this model is abstract
        and should not be created as a separate database table.
    """

    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        unique=True,
        verbose_name='ID',
    )

    class Meta:  # noqa D106
        abstract = True


class Currency(UUIDMixin, models.Model):
    """
    Represents currency exchange rate data.

    This model stores information about currency exchange rates, including the currency code,
    date, and exchange rate.

    Attributes:
        id (uuid.UUID): The UUID serving as the primary key.
        code (str): The code for the currency (e.g., 'USD/EUR').
        date (DateField): The date associated with the exchange rate.
        rate (DecimalField): The exchange rate value.

    Meta:
        verbose_name (str): The singular display name for this model
        in the Django admin interface.
        verbose_name_plural (str): The plural display name for this model
        in the Django admin interface.

    Methods:
        __str__: Returns a string representation of the currency object, using its code.

    Inherits:
        UUIDMixin: A mixin providing a UUID field as the primary key.
    """

    code = models.CharField(max_length=7)
    date = models.DateField()
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:  # noqa D106
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self) -> str:
        """
        Return the code of the currency as its string representation.

        Returns:
            str: The code of the currency (e.g., 'USD/EUR').
        """
        return f'{self.code}'
