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
            'name',
            'source_url'
        )


class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = (
            'email_from',
            'email_to',
            'subject',
            'message'
        )

    def create(self, validated_data):
        from trainingapps.tasks import sending_mail

        sending_mail.delay(
            subject=validated_data.get('subject'),
            email_from=validated_data.get('email_from'),
            email_to=validated_data.get('email_to')
        )

        return super().create(validated_data)
