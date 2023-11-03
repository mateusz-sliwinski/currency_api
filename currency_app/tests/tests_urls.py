# Standard Library
from unittest import TestCase

# Django
from django.urls import reverse


class TestUrls(TestCase):
    def test_currency_url_reverse(self):
        url = reverse('currency')
        self.assertEqual(url, '/currency/')
