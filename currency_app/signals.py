from django.apps import apps
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User
import yfinance as yf
from datetime import date
from currency_app.models import Currency, ExchangeRate


@receiver(post_migrate)
def create_tiers_and_superuser(sender, **kwargs):
    if not User.objects.all():
        superuser = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin')
        superuser.save()

    if not ExchangeRate.objects.all():
        currency_pairs = ['USD/EUR', 'USD/JPY', 'USD/GBP']

        for currency_pair in currency_pairs:
            base_currency_code, target_currency_code = currency_pair.split('/')
            currency_pair_with_suffix = f'{currency_pair}=X'
            download_data = currency_pair_with_suffix.replace('/', '')

            base_currency, created = Currency.objects.get_or_create(code=base_currency_code)

            target_currency, created = Currency.objects.get_or_create(code=target_currency_code)

            data = yf.download(download_data)
            for idx, row in data.iterrows():
                ExchangeRate.objects.create(
                    currency_from=base_currency,
                    currency_to=target_currency,
                    date=date(idx.year, idx.month, idx.day),
                    rate=row['Close']
                ).save()
