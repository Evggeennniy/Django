from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from api.v1 import throttles
# ^ Work with rest framework

from trainingapps import models
from api.v1 import serializer
# ^ Work with serializer

from drf_excel.renderers import XLSXRenderer
from drf_excel.mixins import XLSXFileMixin
# ^ Work with dfr_excel export render

from api.v1 import pagination
from api.v1 import filters as viewfilters

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters, status
from rest_framework.response import Response


class RateViewSet(XLSXFileMixin, viewsets.ModelViewSet):
    queryset = models.Rate.objects.get_queryset().order_by('id')
    serializer_class = serializer.RateSerializer

    renderer_classes = [JSONRenderer, XLSXRenderer]
    filename = 'rate_datas.xlsx'
    # ^ Setted finename to exporting and rederer classes.

    pagination_class = pagination.RatePagination

    filterset_class = viewfilters.RateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )

    ordering_fields = ['id', 'buy', 'sale']
    # ^ Sorting by 'ordering=id' or 'ordering=id,buy'
    # Sorting by criteria, from largest to smallest, if necessary, on the contrary, add '-' before the argument

    throttle_classes = [throttles.AnonCurrencyThrottle]
# ^ This class performs all actions that were available in the classes above.


class SourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Source.objects.get_queryset().order_by('id')
    serializer_class = serializer.SourceSerializer

    pagination_class = pagination.SourcePagination

    filterset_class = viewfilters.SourceFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )

    ordering_fields = ['id', 'name']

    throttle_classes = [throttles.AnonCurrencyThrottle]


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.get_queryset().order_by('id')
    serializer_class = serializer.ContactUsSerializer

    pagination_class = pagination.SupportPagination

    filterset_class = viewfilters.ContactUsFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )

    search_fields = ['username', 'email']
    # ^ Search filter fields - ?search=Benner

    # The search behavior may be restricted by prepending various characters to the search_fields.

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.

    # For example:
    # search_fields = ['=username', '=email']

    ordering_fields = ['id', 'email_from', 'email_to', 'subject']

    throttle_classes = [throttles.AnonSupportsThrottle]

    def create(self, validated_data):

        validdata = validated_data.data
        serializer = self.get_serializer(data=validdata)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        subject = validdata.get('subject')
        email_from = validdata.get('email_from')
        email_to = validdata.get('email_to')
        self.sending_mail(subject, email_from, email_to)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def sending_mail(self, subject, email_from, email_to):
        from trainingapps.tasks import sending_mail

        sending_mail.delay(
            subject=subject,
            email_from=email_from,
            email_to=email_to
        )


# # class RatesView(generics.ListAPIView, generics.CreateAPIView):
# class RatesView(generics.ListCreateAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
#     # ^ Setting a working queryset, and a serializer that will process them
# # ^ Get all view, post new data.


# class RateDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
# # ^ Get id, update id, destroy id.


# def api_get_rate_list(self):
#     import json

#     queryset = Rate.objects.all()

#     response_content = []
#     for object in queryset:
#         response_content.append({
#             'id': object.id,
#             'buy': float(object.buy),
#             'sell': float(object.sell),
#         })

#     # return HttpResponse(json.dumps(response_content), content_type='application/json')
#     return JsonResponse(response_content, safe=False)
