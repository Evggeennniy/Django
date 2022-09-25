from rest_framework.serializers import ModelSerializer
from trainingapps import models


class RateSerializer(ModelSerializer):
    class Meta:
        model = models.Rate
        fields = (
            'id',
            'ccy',
            'base_ccy',
            'buy',
            'sell',
            'source'
        )
# ^ Validation of the data is carried out as in the form, but the purpose of data reassembly,
# and preparation for the api format.


class SourceSerializer(ModelSerializer):
    class Meta:
        model = models.Source
        fields = (
            'id',
            'name',
            'source_url'
        )


class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = (
            'id',
            'email_from',
            'email_to',
            'subject',
            'message'
        )
