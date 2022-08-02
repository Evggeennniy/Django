from django.db import models
from trainingapps.model_choises import CurrencyType

# Create your models here.


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=30)
    email_to = models.EmailField(max_length=30)
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=120)
# ^ A model is a relationship between a class and a database with fields in it.
# Model fields describe columns of the same name in the table and are properties at the same time


class Rate(models.Model):
    ccy = models.CharField(max_length=5, choices=CurrencyType.choices)
    base_ccy = models.CharField(max_length=5, choices=CurrencyType.choices, default=CurrencyType.CURRENCY_TYPE_UAH)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sell = models.DecimalField(max_digits=10, decimal_places=2)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
