# do not import from programm
from django.db import models
from settings.settings import EMAIL_HOST_USER


class CurrencyType(models.TextChoices):
    CURRENCY_TYPE_UAH = "UAH", "Hhivna"
    CURRENCY_TYPE_USD = "USD", "United States Dollar"
    CURRENCY_TYPE_EUR = "EUR", "Euro"
    CURRENCY_TYPE_BTC = "BIT", "Bitcoin"
# ... = "Meaning what comes", "What the user sees"
# ^ Create a selection constraint for a field, and connect in models.py ...(choices=self.choices)
# or this non-class
# CURRENCY_TYPE_UAH = "UAH"
# CURRENCY_TYPE_USD = "USD"
# CURRENCY_TYPE_EUR = "EUR"
# CURRENCY_TYPE_BTC = "BIT"

# CURRENCY_TYPES = (
#     (CURRENCY_TYPE_UAH, "Hhivna"),
#     (CURRENCY_TYPE_USD, "United States Dollar"),
#     (CURRENCY_TYPE_EUR, "EURO"),
#     (CURRENCY_TYPE_BTC, "Bitcoin"),
# )


class EmailUse(models.TextChoices):
    EMAIL1 = EMAIL_HOST_USER, EMAIL_HOST_USER
