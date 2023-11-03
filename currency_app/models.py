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
    code = models.CharField(max_length=7)
    date = models.DateField()
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self) -> str:
        return f'{self.code}'
