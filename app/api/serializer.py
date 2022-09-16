from rest_framework.serializers import ModelSerializer
from trainingapps.models import Rate


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
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
