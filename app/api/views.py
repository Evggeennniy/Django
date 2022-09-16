from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
# ^ Work with rest framework

from trainingapps.models import Rate
from api.serializer import RateSerializer
# ^ Work with serializer

from drf_excel.renderers import XLSXRenderer
from drf_excel.mixins import XLSXFileMixin
# ^ Work with dfr_excel export render


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


class RateViewSet(XLSXFileMixin, viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    renderer_classes = [JSONRenderer, XLSXRenderer]
    filename = 'rate_datas.xlsx'
    # ^ Setted finename to exporting and rederer classes.
# ^ This class performs all actions that were available in the classes above.


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
