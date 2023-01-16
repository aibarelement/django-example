from django.db import models

from accounts import constants


class Account(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def wallet_total_price(self):
        return sum(w.amount for w in self.wallets)


class Wallet(models.Model):
    account = models.ForeignKey(
        to=Account,
        on_delete=models.SET_NULL,
        null=True,
        related_name='wallets'
    )
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    amount_currency = models.CharField(
        max_length=3,
        choices=constants.AmountCurrencyChoices.choices,
        default=constants.AmountCurrencyChoices.KZT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
