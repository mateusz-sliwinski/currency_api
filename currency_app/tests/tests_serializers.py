# Standard Library
import datetime
from unittest import TestCase

# Project
from currency_app.models import Currency
from currency_app.serializers import CurrencySerializer


class CurrencySerializerTestCase(TestCase):
    def setUp(self):
        self.currency_data = {
            'code': 'USD/EUR',
            'date': '2023-11-03',
            'rate': '1.1000',
        }
        self.currency = Currency.objects.create(**self.currency_data)
        self.serializer = CurrencySerializer(instance=self.currency)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'code', 'date', 'rate'})

    def test_serialization(self):
        expected_data = {
            'id': str(self.currency.id),
            'code': 'USD/EUR',
            'date': '2023-11-03',
            'rate': '1.1000',
        }
        self.assertEqual(self.serializer.data, expected_data)

    def test_deserialization(self):
        data = {
            'code': 'EUR/GBP',
            'date': '2023-11-04',
            'rate': '0.8900',
        }
        serializer = CurrencySerializer(data=data)
        self.assertTrue(serializer.is_valid())
        currency_instance = serializer.save()
        self.assertEqual(currency_instance.code, 'EUR/GBP')
        self.assertEqual(currency_instance.date, datetime.date(2023, 11, 4))
        self.assertEqual(str(currency_instance.rate), '0.8900')

    def tearDown(self):
        self.currency.delete()
