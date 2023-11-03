import uuid
from django.test import TestCase
from rest_framework.exceptions import ValidationError

from currency_app.models import Currency


class UUIDMixinTest(TestCase):
    def test_uuid_field_generation(self):
        instance = Currency(code='USD', date='2023-11-08', rate=0.40)
        instance.save()

        self.assertTrue(isinstance(instance.id, uuid.UUID))

    def test_uuid_field_uniqueness(self):
        instance1 = Currency(code='USD', date='2023-11-08', rate=0.40)
        instance2 = Currency(code='USD', date='2023-11-08', rate=0.40)
        instance1.save()
        instance2.save()

        self.assertNotEqual(instance1.id, instance2.id)


class CurrencyModelTestCase(TestCase):
    def setUp(self):
        self.currency = Currency.objects.create(code='USD/EUR', date='2023-11-03', rate='1.1000')

    def test_string_representation(self):
        expected_string = 'USD/EUR'
        self.assertEqual(str(self.currency), expected_string)

    def test_verbose_names(self):
        self.assertEqual(Currency._meta.verbose_name, 'Currency')
        self.assertEqual(Currency._meta.verbose_name_plural, 'Currencies')

    def test_currency_attributes(self):
        self.assertEqual(self.currency.code, 'USD/EUR')
        self.assertEqual(self.currency.date, '2023-11-03')
        self.assertEqual(str(self.currency.rate), '1.1000')

    def tearDown(self):
        self.currency.delete()
