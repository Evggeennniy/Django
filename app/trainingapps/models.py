from django.db import models
from django.utils import timezone
from trainingapps.model_choises import CurrencyType, EmailUse, Modules
# Create your models here.


class CreatedModel(models.Model):
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
    # Create fields for all


class ContactUs(CreatedModel):
    email_from = models.EmailField(max_length=30, choices=EmailUse.choices, default=EmailUse.EMAIL1)
    email_to = models.EmailField(max_length=30)
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=120)
# ^ A model is a relationship between a class and a database with fields in it.
# Model fields describe columns of the same name in the table and are properties at the same time


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    avatar = models.FileField(upload_to='logo')


class Rate(CreatedModel):
    ccy = models.CharField(max_length=5, choices=CurrencyType.choices)
    base_ccy = models.CharField(max_length=5, choices=CurrencyType.choices, default=CurrencyType.CURRENCY_TYPE_UAH)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sell = models.DecimalField(max_digits=10, decimal_places=2)
    nbu_sell = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # source = models.ForeignKey(Source)
    # For create foreignKey use this ^ or :
    source = models.ForeignKey('trainingapps.Source', on_delete=models.CASCADE, null=True, default=None)
    module_that_processed = models.CharField(max_length=15, choices=Modules.choices, default='User')


class ResponseLog(models.Model):
    response_time = models.DecimalField(max_digits=10, decimal_places=4)
    request_method = models.CharField(max_length=4)
    query_params = models.CharField(max_length=50, null=True)
    ip = models.CharField(max_length=20)
    path = models.CharField(max_length=50)
