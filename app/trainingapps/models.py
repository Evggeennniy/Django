from django.db import models

# Create your models here.


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=30)
    email_to = models.EmailField(max_length=30)
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=120)


class Rate(models.Model):
    ccy = models.CharField(max_length=5)
    base_ccy = models.CharField(max_length=5)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sell = models.DecimalField(max_digits=10, decimal_places=2)
