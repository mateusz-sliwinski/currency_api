import uuid
from django.db import models


class UUIDMixin(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        unique=True,
        verbose_name='ID',
    )

    class Meta:
        abstract = True


class Currency(UUIDMixin, models.Model):
    code = models.CharField(max_length=3, unique=True)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self) -> str:
        return f'{self.code}'


class ExchangeRate(UUIDMixin, models.Model):
    currency_from = models.ForeignKey(Currency, related_name='rates_from', on_delete=models.CASCADE)
    currency_to = models.ForeignKey(Currency, related_name='rates_to', on_delete=models.CASCADE)
    date = models.DateField()
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        verbose_name = 'ExchangeRate'
        verbose_name_plural = 'ExchangeRates'

    def __str__(self) -> str:
        return f'{self.currency_to.code} {self.rate} '
