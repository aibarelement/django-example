from django.db import models


class AmountCurrencyChoices(models.TextChoices):
    RUB = 'RUB', 'рубли'
    KZT = 'KZT', 'тенге'
    USD = 'USD', 'доллары'
