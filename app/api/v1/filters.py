import django_filters
from trainingapps.models import Rate


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': ('gte', 'lte', 'lt', 'gt'),
            'sell': ('gte', 'lte', 'lt', 'gt'),
            'source': ('exact', ),
            'base_ccy': ('exact', ),
            'ccy': ('exact', )
            # ^ exact - everything is included except the next in tuple.
        }
        # ^ Create filter field with modificators
