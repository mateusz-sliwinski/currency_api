from django.test import TestCase
from rest_framework.test import APIClient
from currency_app.models import Currency
from currency_app.serializers import CurrencySerializer
from django.test import override_settings


class CurrencyListViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.currency_data_1 = {
            'code': 'USD/EUR',
            'date': '2023-11-03',
            'rate': '1.1000',
        }
        self.currency_data_2 = {
            'code': 'EUR/GBP',
            'date': '2023-11-04',
            'rate': '0.8900',
        }
        self.currency_1 = Currency.objects.create(**self.currency_data_1)
        self.currency_2 = Currency.objects.create(**self.currency_data_2)

    def test_currency_list_view(self):
        response = self.client.get('/currency/')
        self.assertEqual(response.status_code, 200)

        response_data = response.data.get('results', [])

        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)

        while response.data.get('next'):
            response = self.client.get(response.data['next'])
            response_data.extend(response.data.get('results', []))

        self.assertEqual(len(response_data), len(serializer.data))

        for obj_response, obj_serialized in zip(response_data, serializer.data):
            self.assertEqual(obj_response, obj_serialized)

    def tearDown(self):
        self.currency_1.delete()
        self.currency_2.delete()
