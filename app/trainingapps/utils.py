# low level code this
from trainingapps.models import ResponseLog
from time import time


def response_without_logging(self, request):
    res = self.get_response(request)

    return res


def logging_response(self, request):
    timeron = time()
    res = self.get_response(request)
    timeroff = time()

    req_info = ResponseLog.objects.create(
        response_time=timeroff - timeron,
        request_method=request.method,
        query_params=request.GET,
        ip=request.META.get("REMOTE_ADDR"),
        path=request.path
    )
    # ^ Saving information about requests
    req_info.save()

    return res
