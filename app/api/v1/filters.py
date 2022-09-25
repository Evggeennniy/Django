import django_filters
from trainingapps import models


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = models.Rate
        fields = {
            'buy': ('gte', 'lte', 'lt', 'gt'),
            'sell': ('gte', 'lte', 'lt', 'gt'),
            'source': ('exact', ),
            'base_ccy': ('exact', ),
            'ccy': ('exact', )
            # ^ exact - everything is included except the next in tuple.
        }
        # ^ Create filter field with modificators


class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = models.Source
        fields = {
            'id': ('exact', ),
            'name': ('exact', )
        }


class ContactUsFilter(django_filters.FilterSet):
    class Meta:
        model = models.ContactUs
        fields = {
            'email_from': ('exact', ),
            'email_to': ('exact', ),
            'subject': ('exact', )
        }
