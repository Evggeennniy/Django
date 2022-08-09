from time import time
from trainingapps.models import ResponseLog


class SimpleMiddleware:
    def addlog_get_response(self, request):
        timeron = time()
        response = self.get_response(request)
        timeroff = time()

        ResponseLog.objects.create(
            response_time=timeroff - timeron,
            request_method=request.method,
            query_params=request.GET,
            ip=request.META.get("REMOTE_ADDR"),
            path=request.path
        )
        # ^ Saving information about requests
        # req_info.save()
        # ^ Do not this! is ResponseLog do it.

        return response

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.path.startswith("/admin/") or request.path.startswith("/__debug__"):
            response = self.get_response(request)

            return response

        else:
            response = self.addlog_get_response(request)

            return response

        # Code to be executed for each request/response after
        # the view is called.
