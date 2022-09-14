import django_filters
from trainingapps.models import Rate


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': {'gte', 'lte'},
            'sell': {'gte', 'lte'},
        }
        # ^ Create filter field with modificators
