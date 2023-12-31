"""Signals.py files."""
# Standard Library
from datetime import date

# Django
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# 3rd-party
import yfinance as yf

# Project
from currency_app.models import Currency


@receiver(post_migrate)
def create_tiers_and_superuser(sender, **kwargs):
    """
    Create superuser and initialize currency data after all migrations.

    If no User objects exist, a superuser is created with:
    - Username: 'admin'
    - Email: 'admin@example.com'
    - Password: 'admin'

    If no Currency objects exist, download and store currency data.

    Parameters:
    sender: The sender of the signal.
    **kwargs: Additional keyword arguments provided by the signal.

    Returns:
    None
    """
    if not User.objects.all():
        superuser = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin')
        superuser.save()

    if not Currency.objects.all():

        currency_pairs = ['USD/EUR', 'USD/JPY', 'USD/GBP']

        for currency_pair in currency_pairs:
            currency_pair_with_suffix = f'{currency_pair}=X'
            download_data = currency_pair_with_suffix.replace('/', '')

            data = yf.download(download_data)
            for idx, row in data.iterrows():
                Currency.objects.create(
                    code=currency_pair,
                    date=date(idx.year, idx.month, idx.day),
                    rate=row['Close'],
                ).save()
