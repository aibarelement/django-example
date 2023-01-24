from typing import Protocol, OrderedDict
from decimal import Decimal

from django.db import transaction
from django.db.models import QuerySet, Sum, Q, Avg, Case, When, Value, F, DecimalField
from accounts import models, constants


class AccountReposInterface(Protocol):

    @staticmethod
    def get_accounts(action: str) -> QuerySet[models.Account]: ...

    @staticmethod
    def create_account(data: OrderedDict) -> None: ...


class AccountReposV1:

    @staticmethod
    def get_accounts(action: str) -> QuerySet[models.Account]:
        accounts = models.Account.objects.all()

        if action == 'retrieve':
            accounts = accounts.prefetch_related('wallets').annotate(
                total_amount=Sum(
                    'wallets__amount',
                    filter=Q(wallets__amount_currency__in=(
                        constants.AmountCurrencyChoices.KZT,
                        constants.AmountCurrencyChoices.USD
                    )),
                    default=Decimal(0.0)
                ),
                avg_amount=Avg(
                    'wallets__amount',
                    filter=Q(wallets__amount_currency__in=(
                        constants.AmountCurrencyChoices.KZT,
                        constants.AmountCurrencyChoices.USD
                    )),
                    default=Decimal(0.0)
                ),
                custom_amount=Sum(
                    Case(
                        When(
                            Q(wallets__amount_currency=constants.AmountCurrencyChoices.RUB),
                            then=F('wallets__amount') * 2
                        ),
                        When(
                            Q(wallets__amount_currency=constants.AmountCurrencyChoices.USD),
                            then=F('wallets__amount') * 3
                        ),
                        When(
                            Q(wallets__amount_currency=constants.AmountCurrencyChoices.KZT),
                            then=F('wallets__amount') * 4
                        ),
                        default=Value(Decimal(0.0)),
                        output_field=DecimalField()
                    )
                )
            )

        return accounts

    @staticmethod
    @transaction.atomic
    def create_account(data: OrderedDict) -> None:
        wallets = data.pop('wallets')
        account = models.Account.objects.create(**data)
        models.Wallet.objects.bulk_create([models.Wallet(**w, account=account) for w in wallets])
